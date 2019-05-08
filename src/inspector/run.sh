#!/bin/bash

# paths
LOG_DIR=/data
WORKDIR=/root/work

# image disk
IMAGE=denden047/instagrambot
TAG=latest

# options
NOW=$(date "+%Y%m%d%H%M")
WORKPATH="-w ${WORKDIR}/src"
PORTS=""

# command
if [ $1 = "train" ]; then
    TAG=latest
    # 普通に実行する
    RUN_CMD="mpiexec --allow-run-as-root -np 8 --mca btl ^openib python train.py \
        --agent=KerasPhantomxAgent \
        --env=PhantomxEnv \
        --train-for=1000 \
        --test-for=1 \
        --map-dir=/data/${NOW}/map \
        --tensorboard=/data/${NOW}/tensorboard \
        --i-init=10000 \
        --freq=1000 \
        --max-episode-len=1000 \
        --action-gain=0.785 \
        --action-repeats=1 \
        --steps-per-repeat=5 \
        --limit-update-num=61000 \
        --random-initial-position \
    "
elif [ $1 = "eval" ]; then
    TAG=latest
    PORTS="-p 3000:3000"
    DATA_DIR=/data/201812110903
    # VNCで実行する
    RUN_CMD="mpiexec --allow-run-as-root -np 1 --mca btl ^openib python train.py \
        --eval \
        --render-size-w 720 \
        --render-size-h 480 \
        --monitor ${DATA_DIR}/movie/${NOW}.avi \
        --agent=KerasPhantomxAgent \
        --env=PhantomxEnv \
        --test-for=1 \
        --map-dir=${DATA_DIR}/map \
        --action-gain=0.785 \
        --action-repeats=1 \
        --steps-per-repeat=5 \
        --max-episode-len=1000 \
    "
elif [ $1 = "test" ]; then
    TAG=latest
    PORTS="-p 3000:3000"
    DATA_DIR=/data/201812110903
    # VNCで実行する
    RUN_CMD="python test.py \
        --eval \
        --render-size-w 720 \
        --render-size-h 480 \
        --monitor ${DATA_DIR}/movie/${NOW}.avi \
        --agent=KerasPhantomxAgent \
        --env=PhantomxEnv \
        --test-for=1 \
        --map-dir=${DATA_DIR}/map \
        --action-gain=0.785 \
        --action-repeats=1 \
        --steps-per-repeat=5 \
        --max-episode-len=100 \
    "
elif [ $1 = "calibrate_camera" ]; then
    cd src/real/camera
    python collect_calibration_data.py && \
    python calibration.py
    exit 0
elif [ $1 = "camera" ]; then
    cd src/real/camera
    for i in `seq 1 10`
    do
        echo $i
        sudo python main.py
    done
    exit 0
elif [ $1 = "robot" ]; then
    cd src
    sudo python train.py \
        --mode real \
        --timesteps 1000 \
        --frame-time 0.
    exit 0
elif [ $1 = "test_run" ]; then
    TAG=latest
    PORTS="-p 3000:3000"
    # 普通に実行する
    RUN_CMD="mpiexec --allow-run-as-root -np 1 --mca btl ^openib python train.py \
        --agent=KerasPhantomxAgent \
        --env=PhantomxEnv \
        --train-for=1000 \
        --test-for=1 \
        --map-dir=/data/${NOW}/map \
        --tensorboard=/data/${NOW}/tensorboard \
        --random-initial-position \
        --delay=0.005 \
        --i-init=1000 \
        --freq=1000 \
        --action-gain=0.785 \
        --action-repeats=5 \
        --steps-per-repeat=1 \
        --limit-update-num=2 \
    "
else
    echo 'Please, set option'
    exit 0
fi

# run
nvidia-docker run -it --rm \
    ${OPTS} \
    ${PORTS} \
    ${WORKPATH} \
    -v ${PWD}:${WORKDIR}:ro \
    -v /data2/naoya/DeepRobotics/mmprl:/data \
    ${IMAGE}:${TAG} \
    /bin/bash -c "${RUN_CMD}"
