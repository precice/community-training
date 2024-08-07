# Step 3: Mesh of Fluid domain

In this section we'll generate the Fluid Mesh using using the utility `snappyHexMesh` in OpenFOAM v2406.

## Introduction

The mesh generation process in OpenFOAM consists of several steps. You'll find the required files in the `skeleton` directory, which is more or less structured as a common OpenFOAM case, with the `constant` and `system` folders.
There is no `0` folder as it is not required at this step.

You'll also find two Bash scripts:

- `clean_mesh.sh`: this script allows you to remove all the intermediate and solution files, in case you want to start over with a new computation
- `run_mesh.sh`: this script runs all the required steps in a batch. **Do not use this yet**, as we first need to prepare the respective configuration files.

## Configuring blockMesh

The first task consists in generating the fluid domain. This is achieved by the tool `blockMesh`, which creates the domain and the external boundaries based on the parameters contained in the dictionary `blockMeshDict` in the `system` folder.

### Domain dimension

In this case we create a box:

- 1.5m long in *x* direction (the direction of the freestream)
- with a section of $0.48 \times 0.48$ m in *y* (*lift* direction) and *z* (*span* direction)

If you look at the reference frame of the wing in the `blockMeshDict`, you'll notice that it is placed at the root section at mid chord. So:

- we place the *inlet* face at $x_1 = -0.25$m and the *outlet* face at $x_2 = 1.25$ m.
- we place the wing in the middle of the box in *y* direction, so we place the *y* limits at $y_1 = -0.24$ m and $y_2=0.24$ m.
- finally, we place the root section at $z_1 = 0$ m and the final face at $z_2 = 0.48$ m.

All these parameters are set at lines `24-29` of `blockMeshDict`. For the moment, leave them like this.

### Discretization

Once we have defined the limits, we need to define the number of blocks that we want in each direction. Look for the dictionary entry `blocks` in `blockMeshDict` and locate the terms `NX`, `NY` and `NZ`. These represent the number of cells in which the domain will be divided into in each direction.
We divide the domain into $0.06 \times 0.06 \times 0.06$m cells, so you need to substitute `NX`, `NY` and `NZ` with `25`, `8` and `8` respectively.
The background mesh is quite coarse but for the moment we favor execution speed.

### Boundary conditions

`blockMeshDict` allows you to define the boundary conditions of the domain. The dictionary entry `boundary` defines:

- `inlet`
- `outlet`
- `slip`

## Generating the background mesh

After you have sourced your OpenFOAM, you can run `blockMesh` from the root folder of the case to generate the external domain.

If you want to look at the domain, you can run `paraFoam -block`

(**TODO**: image)


## surfaceFeatureExtract



## decomposePar


## snappyHexMesh


## reconstructParMesh


## checkMesh


