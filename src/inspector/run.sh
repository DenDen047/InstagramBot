#!/bin/bash

# paths
LOG_DIR=/data
WORKDIR=/workdir

# image disk
IMAGE=denden047/instagrambot:latest

# options
WORKPATH="-w ${WORKDIR}/src"

# command
RUN_CMD="python inspector.py"
"

# run
nvidia-docker run -it --rm \
    ${WORKPATH} \
    -v ${PWD}:${WORKDIR}:ro \
    ${IMAGE} \
    /bin/bash -c "${RUN_CMD}"
