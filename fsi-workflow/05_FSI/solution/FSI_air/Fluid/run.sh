#!/usr/bin/env bash
set -e -u

mpirun -np 8 --oversubscribe pimpleFoam -parallel | tee log.pimpleFoam 2>&1
