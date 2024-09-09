# Task 5: FSI simulation

Finally we are able to put everything together and start our **fluid-structure interaction** simulation. We'll use all the work done until now to setup our **Fluid** and **Solid** participants.

## Solid setup

You need to use the mesh generated in step `01_solidMesh`: copy the `.inp` mesh in the current directory.

**NOTE**: Remember to use the one converted in *meters*.

### `solidModel.inp`

Complete the file with the following information: 

- section `*INCLUDE`: replace `YOURMESH.inp` with the actual name of the mesh (`wing2312_m.inp`)
- section `*MATERIAL`: replace the terms `E`, `NU` and  `RHO` with `5.68E8`, `0.46` and `2070` which correspond to a polymeric material close to PTFE
- section `*DYNAMIC`: replace `DT` and `TFINAL` with `1.0E-3` and `0.5`. We perfrom a simulation $0.5$ seconds long with a time-step of $1ms$
- section `*BOUNDARY`: replace `NODESET` with the name given to the msh group of the **root** (`Nroot_Nodes`)
- section `*AMPLITUDE`: replace `RAMPSEQUENCE` with `0.0, 0.05, 0.2, 1.0, 0.5, 1.0`. We ramp the loading of the wing, starting with the $5\%$ of the total load, arriving at $100\%$ after $0.2s$
- section `*CLOAD`: replace each of the `WETSURF` entries with the name of the group given to the **wet surface**(`NwetSurface_Nodes`)

### `config.yaml`

This file contains the information required by the **CalculiX adapter** to connect to **preCICE**. The information here must match the information contained in the `precice-config.xml` file

 - entry `patch`: replace `WETSURF` with the name of the group given to the *wet surface*, **WITHOUT the N at the beginning**  (`wetSurface_Nodes`)

The **Solid participant** is now ready and we can move to the **Fluid participant**.

## Fluid setup

copy mesh

copy U, p, phi

changeDictionary

## Coupled simulation

## Results
