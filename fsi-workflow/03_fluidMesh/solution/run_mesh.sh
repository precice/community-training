#!/bin/sh

blockMesh
# surfaceFeatureExtract
decomposePar
mpirun -np 8 snappyHexMesh -parallel
reconstructParMesh

checkMesh -latestTime |  tee log.checkMesh 2>&1


