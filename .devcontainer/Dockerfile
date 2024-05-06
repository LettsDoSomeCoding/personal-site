FROM mcr.microsoft.com/devcontainers/base:jammy

# Install graphviz and python for diagrams tooling in
RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y install git golang-go graphviz python3 python3-pip xdg-utils

RUN wget -c https://github.com/gohugoio/hugo/releases/download/v0.123.3/hugo_extended_0.123.3_Linux-64bit.tar.gz -O - | tar -xz -C /usr/local/bin hugo

RUN pip3 install diagrams 
