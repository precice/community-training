#!/bin/bash

cd Fluid

cp -r 0.orig 0

decomposePar
#mpirun -np 8 -oversubscribe renumberMesh -overwrite -parallel | tee log.renumberMesh
mpirun -np 8 -oversubscribe simpleFoam -parallel | tee log.solver 2>&1
reconstructPar -latestTime

