#!/bin/bash

cd Fluid

echo "cleaning case..."

rm -rfv 0

echo "remove processor folders"

rm -rfv processor*

echo "remove log files"

rm -rfv log.*

cd ..
