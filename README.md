# README

This is the front page documentation for developing on this project. It should be the starting point for any developer who wants add to the project.

## What is this project?

This is the personal website of Owen Letts (@lettsdosomecoding on GitLab/GitHub), [www.rollagain.net](https://www.rollagain.net). Both the website and this project mainly serve as a means of showing technical aptitude and thus sometimes more experimental and less practical technologies may be employed for the sake of learning.

The project contains the source code for the website which is built using Hugo, a static website generator written in GO. It uses the Academic theme originally created by [George Cushen](https://georgecushen.com/).

## Getting Started

### Dev Environment Setup

The requirements to build the website are all contained with a dockerfile so that it can be used with any IDE. Further explaination of this choice is talked about in the [build design documentation](/docs/build-design.md). The suggested IDE and OS environment is VSCode and Linux respectively, and thus the instruction for setup will only cover this specification. The is also an assumption that Docker is installed.

1. Start up VSCode and install the VSCode [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
2. Bring up the VSCode command palette (Ctrl + Shift + P) and search for `Dev Containers: Open Folder in Container...` and run it whilst choosing the folder you have cloned this project into
3. Let the container build and all requirements should be pre-installed and ready to use

### Building the Website

Documentation for building and developing Hugo websites more generally can be found [here](https://gohugo.io/getting-started/usage/), however the one command you really need to know is `hugo server`, which should produce output similar to the following:

```
$ hugo server
hugo: downloading modules …
hugo: collected modules in 8095 ms
Watching for changes in /home/vscode/.cache/hugo_cache/modules/filecache/modules/pkg/mod/github.com/!hugo!blox/hugo-blox-builder/modules/{blox-bootstrap,blox-plugin-netlify@v1.1.2-0.20240507194415-7d5cbf3ce7a1,blox-plugin-reveal@v1.1.2}
Watching for changes in /workspaces/personal-site/{assets,content,data,static}
Watching for config changes in /workspaces/personal-site/config/_default, /home/vscode/.cache/hugo_cache/modules/filecache/modules/pkg/mod/github.com/!hugo!blox/hugo-blox-builder/modules/blox-plugin-netlify@v1.1.2-0.20240507194415-7d5cbf3ce7a1/config.yaml, /home/vscode/.cache/hugo_cache/modules/filecache/modules/pkg/mod/github.com/!hugo!blox/hugo-blox-builder/modules/blox-plugin-reveal@v1.1.2/config.yaml, /home/vscode/.cache/hugo_cache/modules/filecache/modules/pkg/mod/github.com/!hugo!blox/hugo-blox-builder/modules/blox-bootstrap/v5@v5.9.7/hugo.yaml, /workspaces/personal-site/go.mod
Start building sites … 
hugo v0.123.3-a75a659f6fc0cb3a52b2b2ba666a81f79a459376+extended linux/amd64 BuildDate=2024-02-23T17:09:20Z VendorInfo=gohugoio


                   | EN   
-------------------+------
  Pages            |  41  
  Paginator pages  |   0  
  Non-page files   |  30  
  Static files     |  12  
  Processed images | 125  
  Aliases          |  13  
  Cleaned          |   0  

Built in 484 ms
Environment: "development"
Serving pages from disk
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1) 
Press Ctrl+C to stop
```

You will then be able to make adjustments to the code and the server will automatically rebuild the website to reflect these changes, which you can preview at `http://localhost:1313/`.

### Dev Branching Workflow

As there will only ever be one version of this project that is in use, the `HEAD` commit on the `main` branch will be the production version. Thus the branching workflow will be:

1. Create dev branch off of `main` branch, named descriptively
2. Make changes and commit to dev branch
3. When changes have been finished, fetch and merge any changes to the `main` onto your dev branch and resolve any conflicts
4. Repeat `step 3` if changes have happened in between conflict resolution
5. Create a Merge/Pull request for the main branch and request review from `@lettsdosomecoding`
6. Once approved and CI has passed the dev branch will be rebased onto `main` to preserve the development history

### Documentation

Documentation outside of this page should be held in the `/docs` folder. This folder holds the documents themselves as Markdown documents in the root and the images used in the documents in the `./images` folder. Also held in the images folder is and scripts used for image generation, which in the case of this project uses the python module `Diagrams`. [Diagrams](https://diagrams.mingrammer.com/) is a "Diagram as code" tool for creating system designs by writing python code and then building it. The key advantage is that it makes design diagrams editable in a more Git friendly way, allowing for easy versioning and rollback of design to previous versions.

### Deployment

The detailed description for how deployment is architected and its reasoning can be found in the [build design doc](docs/build-design.md). The elevator pitch is that deployment happens via a CI/CD pipeline on GitLab and only occurs on the main dev branch, which then deploys it to GitLab Pages.

## License

Copyright © 2017-present Owen Letts. This work is licensed under [CC BY NC ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0)

Released under the [MIT](https://gitlab.com/lettsdosomecoding/personal-site/-/blob/main/LICENSE.md) license.