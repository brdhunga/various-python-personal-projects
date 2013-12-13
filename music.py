#!/usr/bin/env python

"""
Compartmentalizes music, images, videos and documents into different directories. 
"""

import os
import argparse
import glob
import shutil


parser = argparse.ArgumentParser(description='Compartmentalizes music, images, videos \
and documents into different directories.')
parser.add_argument('-s',
                    '--source',
                    help='The source directory. In absense of \
directories provided, it creates \
relevant directories in the source',
                    required=True)
parser.add_argument('-m',
                    '--music',
                    help='The music directory',
                    default='music',
                    required=False)
parser.add_argument('-p',
                    '--pictures',
                    help='The pictures directory',
                    default='pictures',
                    required=False)
parser.add_argument('-v',
                    '--videos',
                    help='The videos directory',
                    default='videos',
                    required=False)
parser.add_argument('-d',
                    '--documents',
                    help='The documents directory',
                    default='documents',
                    required=False)

args = parser.parse_args()
os.chdir(args.source)


# relocation file parameters

music = glob.glob("*.mp3") + \
        glob.glob("*.flac") + \
        glob.glob("*.aac")        

pictures = glob.glob("*.jpg") + \
           glob.glob("*.JPG") + \
           glob.glob("*.jpeg") + \
           glob.glob("*.JPEG") + \
           glob.glob("*.jpe") + \
           glob.glob("*.JPE") + \
           glob.glob("*.png") + \
           glob.glob("*.bmp") + \
           glob.glob("*.xcf") + \
           glob.glob("*.psd") + \
           glob.glob("*.gif") 

videos = glob.glob("*.avi") + \
         glob.glob("*.mp4") + \
         glob.glob("*.flv") + \
         glob.glob("*.mkv") + \
         glob.glob("*.divx") + \
         glob.glob("*.mov")

documents = glob.glob("*.pdf") + \
            glob.glob("*.PDF") + \
            glob.glob("*.zip") + \
            glob.glob("*.doc") + \
            glob.glob("*.xls") + \
            glob.glob("*.ppt") + \
            glob.glob("*.docx") + \
            glob.glob("*.xlsx") + \
            glob.glob("*.pptx") + \
            glob.glob("*.odt") + \
            glob.glob("*.m")


# Deletes the original after copying. 

for songs in music:
    if not os.path.exists(args.music):
        os.mkdir(args.music)
    shutil.copy(songs, args.music)
    os.remove(songs)

for video in videos:
    if not os.path.exists(args.videos):
        os.mkdir(args.videos)
    shutil.copy(video, args.videos)
    os.remove(video)

for picture in pictures:
    if not os.path.exists(args.pictures):
        os.mkdir(args.pictures)
    shutil.copy(picture, args.pictures)
    os.remove(picture)

for document in documents:
    if not os.path.exists(args.documents):
        os.mkdir(args.documents)
    shutil.copy(document, args.documents)
    os.remove(document)