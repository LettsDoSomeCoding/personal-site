---
title: "Evolving this Website"
subtitle: "Change is inevitable and should be embraced!"
tags: ["website", "Technical", "Hugo", "Academic"]
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
projects: ["personal-site"]
---

Before I could start creating new content for this site I had to change a lot to get it working again, to be in a more reliable situation going forward and to make it a project I was proud to show off. In this article I will be going over all the various changes I made and brief explanation of why I made the change.

# What has Changed?

## Cloned to GitHub

The code for this site is now cloned on both GitLab (the main site for contribution) and GitHub (it is push cloned here). The reason for this is that GitLab is used less by the software development community, so adding a copy to GitHub makes the project more discoverable. It also gives the added benefit that there is an extra copy of the code, just in case of a GitLab outage or a security breach of GitLab that could place the code in jeopardy.

## Dockerised Development Environment and Streamlining setup

Getting from pulling down the code to being able to build and test the code was a bit of a pain, especially when moving from one PC to another. To help with this issue I've added the devcontainer. This works with the VSCode Remote Development Extension pack natively and VSCode will ask on startup whether you want to develop in the container. This means that all the requirements for doing all the relevant development tasks related to this project will be available from the get go, and it will also add consistency of environment so that you don't get the classic addage "It works on my machine". To make it as usable as possible for developers regardless of IDE, I have made sure to add as many of the project requirements into the DOCKERFILE so that others can take that and use it with their preferrable configuration.

{{<figure src="docker.png" caption="Happy whales make for happy developers">}}

## Updating to a Newer Version of Hugo and Academic

When I came back to this project nothing would build and Netlify (the previous host) couldn't deploy the website. It turns out if you don't update things over several years you get left behind and things become deprecated. Who knew! So there was quite a lot of adjustments to be made. The way that the academic theme was built and applied was completely different now, using the HugoBlox framework, Tailwind CSS, and wowchemy JS. This meant a complete restructure of the code, going from TOML to YAML config files, and migrating where each section of config was located. This was a hard requirement as there was new functionality and being out-of-date leaves the website vulnerable to exploits. I'm glad to be on the other side and will be taking a more iterative approach going forward.

## Added Giscus Commenting

One thing that was missing from my previous version of the site was an easy way to provide feedback. I had a contact form, which did genuinely get some useful feedback and nice comments about how I helped people, but wasn't conversational. Thus I've implemented [Giscus](https://giscus.app/) in it's stead, so that people can comment directly on the posts. It took some fiddling around with the configuration but I'm very happy with the result.

## Deploy via GitLab Pages

As mentioned already, this site used to be deployed using Netlify. Whilst this was very easy and I would recommend Netlify for most static site deployments, especially for people who are less comfortable with writing scripts. However, I wanted to show that I can write a CI/CD script and I wanted to make sure that I could block the deployment with tests. I still wanted the deployment to be cost-free as this is a personal project though. So I went with GitLab Pages. A free hosting option provided by GitLab, that also comes with niceties like CloudFlare protection. If you want to see the deployment code, then feel free to take look at the [.gitlab-ci.yml file](https://gitlab.com/LettsDoSomeCoding/personal-site/-/blob/main/.gitlab-ci.yml). I'd also be happy to recieve any feedback.

{{<figure src="happy-owen.jpeg" caption="How I look when I get feedback on my projects">}}

That being said I do plan on changing my deployment method quite often so that I can learn and experiement with other technologies, so don't get too attached.

## Added Documentation

No matter how technically amazing your setup is, it will become unusable without documentation. I made good documentation a priority here. Starting with the README, giving people a starting point to use the repository, to more architectural documentation, describing the project setup but also explaining why it is the way it is. This gives great context for anyone new to the code.

# Evolution not Revolution

There were multiple times where I thought "Maybe I should start over with a completely different setup". Maybe move away from Academic and Hugo, or host everything myself. But I realised that this would be introducing scope creep to the project. Adding unnecessary complexity and increasing the size of the task to something that I would never complete. That doesn't mean I won't expand to more experimental deployments in the future but lets go slower, steadier and be pragmatic.