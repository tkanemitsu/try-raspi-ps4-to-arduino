# https://hub.docker.com/layers/library/ubuntu/25.04/images/sha256-a94f2d41a126942baaecffc7d783beadba6f5255840d97514d5358e4eae4bdf9
FROM ubuntu:25.04

RUN apt update \
 && apt-get install -y ca-certificates wget clang

RUN apt update \
 && apt-get install -y unzip

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
 && apt-get install -y ./google-chrome-stable_current_amd64.deb \
 && rm ./google-chrome-stable_current_amd64.deb

RUN apt update \
 && apt-get install -y sudo \
 && gpasswd -a ubuntu sudo \
 && echo 'ubuntu ALL=NOPASSWD: ALL' >> /etc/sudoers

RUN apt update \
 && apt-get install -y git

# evdev が gcc を利用
RUN apt update \
 && apt-get install -y gcc make cmake meson build-essential

# evdev が Python.h を利用
RUN apt update \
 && apt-get install -y python3-dev

USER ubuntu

RUN git config --global core.filemode false

# https://docs.astral.sh/uv/getting-started/installation/
RUN wget -qO- https://astral.sh/uv/install.sh | sh
