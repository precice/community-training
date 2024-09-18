#!/usr/bin/env bash
set -e -u

rm -rfv 0
cp -r 0.orig 0

echo "Changing U dictionary"
changeDictionary 2>&1 | tee log.changeDict

decomposePar -force
