FROM mcr.microsoft.com/devcontainers/cpp:0-ubuntu-20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install --no-install-recommends git python3-dev python3-numpy libhdf5-openmpi-dev
ENV PYTHONEXE=python3
ENV HDF5_ROOT_DIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
