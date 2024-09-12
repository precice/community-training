#!/bin/bash
cd ${0%/*} || exit 1    		    		# Run from this directory
. $WM_PROJECT_DIR/bin/tools/RunFunctions    # Tutorial run functions

mpirun -np 8 --oversubscribe pimpleFoam -parallel | tee log.pimpleFoam 2>&1
