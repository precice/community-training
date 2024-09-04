#!/bin/sh

rm -rfv processor*
cd constant

cd triSurface
rm -rfv *.eMesh
rm -rfv *.obj
cd ..

rm -rfv polyMesh
rm -rfv extendedFeatureEdgeMesh

cd ..
