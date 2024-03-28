FROM mcr.microsoft.com/devcontainers/base:jammy

# Install graphviz and python for diagrams tooling in
RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y install git graphviz hugo python3 python3-pip xdg-utils

RUN pip3 install diagrams 
