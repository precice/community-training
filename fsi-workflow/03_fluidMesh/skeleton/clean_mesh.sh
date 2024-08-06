#!/bin/sh

rm -rfv processor*
cd constant

cd triSurface
rm -rfv *.eMesh
cd ..

rm -rfv polyMesh
rm -rfv extendedFeatureEdgeMesh

cd ..
