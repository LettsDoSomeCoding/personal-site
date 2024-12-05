---
title: "New Project. The Instagram Story Cutter!"
subtitle: "There is probably a tool for this already..."
tags: ["project", "Technical", "Python", "Vlog", "Programming"]
date: 2024-10-12
draft: true

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

Throughout my travels across East Asia and South America I created many Instagram stories, that my followers surely enjoyed. However, one annoyance I had was that stories can only be sixty seconds long, whilst my regaling of facts and observations of cultural phenomena can't be held seldom to such a constraint. So I had to manually cut my videos to instances of sixty seconds each. A tedious task. And thus gives birth to my Instagram Story Cutter project!

# Starting Simple

I often have grand ideas for application but then never finish them because it takes too long to get something that gives tangible benefit. NOT THIS TIME! I'm keeping the requirements simple.

*Hard Requirements:*
 - An app that takes a video and cuts it into sixty second clips
 - Do it right! Well structured code, with automated unit tests run in continuous integration
 - That's it!

*Some stretch goals if they come by easily*
 - Remove any silence at the start of the first clip

In order to keep any scope creep from coming in I decided to leave this first iteration of the app as a commandline utility. I thought writing in Python would be sensible, so that I'm not trying out too many new technologies at once, whilst sprucing up on my Python knowledge.

# Decisions, Decisions!

As with any project, there are many permutations one can take to solve the problem. So I'm outlining some of the options I found and why I chose the ones that I ended up using.

## CLI Module

There is a wide plethora of different packages one can choose for implementing their command line interface (CLI). My main objective was minimize on the boiler plate code and let the package do the work for me.

### The standard library approach

This requires the most code to get a CLI that is fully functional. This is with good reason though, it gives the most flexibility and fundamentally any other CLI package will be using the standard library methods underneath. It also means that you don't require any packages as dependencies and it will be maintained as long as Python remains relevant as a language. But it didn't fit my mantra for simplistic code so let's move one.

### Click

A very nice package that uses decorators on functions to define the CLI usage. I've used click in the past and been very happy with it. It's still explicit in it's configuration so there isn't much hidden away from the developer, and it bundles in a bunch of the standard options that you would want your CLI to have, like setting up help text automatically. But it just didn't scratch that simplicity itch enough.

### Typer

In comes Typer! Lord of simplicity, king of the lazy CLI developer. With a single import and a slight adjustment in the \_\_name\_\_ function and Bob's your uncle. A fully functioning CLI with arguments based on the internal python function. NO BOILERPLATE NEEDED! This was the winner for me and although I could see the lack of explicit configuration being slightly less readable or obvious for another developer in the future, I think it was worth it for this small individual project.

## Video editing in Python

Audio and video manipulation is complex. Not only are there many different formats of video and audio encoding, but there are also all the many different ways of combining those various components together with different metadata, compression and compatability. Also, what you want to do with all those options can vary a lot dependent on use case so choosing the best python package for me took some experimentation and learning.

### OpenCV

OpenCV is often mentioned for video manipulation however most tutorials revolve around the use of this library to create videos by capturing from a camera. So it appears to be more for computer vision use cases and video analysis rather than standard video editing. Useful for certain applications and I'm glad I've discovered it but not right for this project.

### MoviePy

MoviePy initially seemed like a great option. Plenty of other  I also came across an issue where the video would come out the wrong aspect ratio. This seems to be a bug that has cropped up multiple times in moveipy's history but hasn't been fixed in all cases. It doesn't look like it will be soon either as contributions are far and few between nowadays.

### py-ffmpeg

So one Uses ffmpeg directly but requires installation of ffmpeg

### PyAV

A binding to the FFmpeg  libraries that means no need to sinstall FFmpeg yourself but if installing via Pip you are using the version of FFmpeg that it was compiled with.

It does also say this `If the ffmpeg command does the job without you bending over backwards, PyAV is likely going to be more of a hindrance than a help.`

This seems to be the best option and with help from AI I managed to find a solution.


## How FFmpeg works



## How AI helped me solve my problems

Claude didn't understand how to use filters but did give better initial code

ChatGPT knew more about PyAV but was sometimes generic with it's answers and required extra prompting.

Intellicode was ok. Sometimes it would give suggestions when I just wanted tabs and sometimes the suggestions weren't useful. Other times it gave better suggestions. Overall I think it helps to reduce my carpal tunnel.


# Future Roadmap
