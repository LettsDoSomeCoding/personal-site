---
title: "New Project. The Instagram Story Cutter!"
subtitle: "There is probably a tool for this already..."
tags: ["project", "Technical", "Python", "Vlog", "Programming"]
date: 2024-10-12
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Documentation is key!"
  focal_point: "Centre"
  placement: 3
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["instagram-story-cutter"]
---

# Starting simple with a Python CLI


## Which CLI library

### Typer

Initial choice as it seems simple but already customisation of naming and documentation requires extra typing so why is this better than click?

## Video editing in Python

### OpenCV

Most tutorials revolve around the use of this library to create a new video by capturing from a camera. Appears to be more for computer vision use cases. Useful but maybe overkill for this project.

### py-ffmpeg

Uses ffmpeg directly but requires installation of ffmpeg

### PyAV

A binding to the FFmpeg  libraries that means no need to sinstall FFmpeg yourself but if installing via Pip you are using the version of FFmpeg that it was compiled with.

It does also say this `If the ffmpeg command does the job without you bending over backwards, PyAV is likely going to be more of a hindrance than a help.`

This seems to be the best option and with help from AI I managed to find a solution.

### MoviePy

The easiest to use potentially and plenty of tutorials but not quite as powerful as ffmpeg based libraries and actually uses ffmpeg under the hood. I also came across an issue where the video would come out the wrong aspect ratio. This seems to be a bug that has cropped up multiple times in moveipy's history but hasn't been fixed in all cases. It doesn't look like it will be soon either as contributions are far and few between nowadays.

## How FFmpeg works



## How AI helped me solve my problems

Claude didn't understand how to use filters but did give better initial code

ChatGPT knew more about PyAV but was sometimes generic with it's answers and required extra prompting.

Intellicode was ok. Sometimes it would give suggestions when I just wanted tabs and sometimes the suggestions weren't useful. Other times it gave better suggestions. Overall I think it helps to reduce my carpal tunnel.


# Future Roadmap
