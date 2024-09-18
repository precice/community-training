#!/usr/bin/env sh
set -e -u

echo "clean CalculiX case"
rm -fv ./*.cvg ./*.dat ./*.frd ./*.sta ./*.12d ./*.rout spooles.out dummy
rm -fv *.vtu
rm -fv *.pvd

rm -rfv ./convert

