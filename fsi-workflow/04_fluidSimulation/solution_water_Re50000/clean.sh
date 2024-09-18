#!/usr/bin/env bash
set -e -u

echo "cleaning case..."

rm -rfv 0

echo "remove processor folders"

rm -rfv processor*

echo "remove post processing folder"

rm -rfv postProcessing

echo "remove log files"

rm -rfv log.*
