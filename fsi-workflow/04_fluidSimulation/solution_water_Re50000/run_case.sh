#!/bin/bash

cd Fluid

cp -r 0.orig 0

decomposePar
mpirun -np 8 simpleFoam -parallel | tee log.solver
reconstructPar -latestTime

