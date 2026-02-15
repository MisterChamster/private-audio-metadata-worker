# Audio Metadata Worker

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Additional notes](#additional-notes)

## Introduction
This is my private program made for printing and appending metadata (album, tracknum, title, artist, date) to audio files. It allows for group changing for whole directory as well as recurring in child folders. Also allows smart appending of specific metadata types.

## Features
- Printing file metadata
- Appending metadata to audio files
- Smart appending options
- Works for single files and whole folders
- Simple and easy to use
- Lightweight

## Installation
```bash
git clone https://github.com/MisterChamster/private-audio-metadata-worker.git audio-mtd-worker
cd audio-mtd-worker
```

## Usage
```bash
#Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
```bash
#Linux/macOS
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Additional notes
I wanted to write this program for myself for a looong time. Feel free to use it yourself!
