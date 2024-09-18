#!/usr/bin/env bash
set -e -u

echo "Cleaning case..."
rm -rfv 0
rm -rfv processor*
rm -rfv postProcessing
rm -rfv log.*
rm -rfv precice-profiling
