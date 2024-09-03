#!/bin/bash
cd ${0%/*} || exit 1    		    		# Run from this directory
. $WM_PROJECT_DIR/bin/tools/RunFunctions    # Tutorial run functions


mbdyn-esm-adapter -f config.json > log.esm 2>&1 &
ESM_PID=$! 
echo "esm adapter PID is $ESM_PID" 


casename="Fluid"
mpirun -np 8 renumberMesh -overwrite -parallel -case ${casename} > log.renumber 2>&1
mpirun -np 8 pimpleFoam -parallel -case ${casename} > log.pimpleFoam 2>&1

