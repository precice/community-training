# Task 5: FSI simulation

Finally we are able to put everything together and start our **fluid-structure interaction** simulation. We'll use all the work done until now to setup our **Fluid** and **Solid** participants. The starting point of our case is in the `skeleton` folder, which is the root of our FSI case.

## Solid setup

Enter the `Solid` folder.


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

Now go back to the root of the case and enter the `Fluid` folder. This is an usual `OpenFOAM` case that you have to configure.

### `constant` folder

In this folder you need to:

- copy our previously generated mesh: copy the `polyMesh` folder from your `0.003` folder in `03_fluidMesh/skeleton` (or from the `constant` folder in `04_fluidSimulation/skeleton/Fluid`)
- open the `dynamicMeshDict` and replace `WETSURF` in the `displacementLaplacianCoeffs` dictionary entry with the name given to the wing patch (`naca2312`). This dictionary tells OpenFOAM that we need a mesh motion solver to perform our FSI simulation

### `0.orig` folder

Create a folder named `0.orig` in the `Fluid` folder. Copy here the files:

- `U`
- `p`
- `phi`

that you have saved in `04_fluidSimulation/skeleton/results/water/500`. We are initializing the fluid domain with our previous solution.

### update of `U` file

When we performed the the fluid simulation, in the `U` file for the initial conditions, we defined the surface of the wing as `noSlip`. This boundary condition remains through all your simulation and it is the current BC in the `U` file that you copied. In **FSI** simulations, it would give you wrong results. The correct BC is `movingWallVelocity`. To avoid opening a large file to look for a boundary condition, you can use the utility `changeDictionary`. You have to:

- open the file `changeDictionaryDict` in the `system` folder
- in the `boundaryField` dictionary entry, look for `PATCH` and replace it with `naca2312` and the entry `TYPE` with `movingWallVelocity`. You will update the boundary condition before running the coupled simulation.

### `system` folder

Open the `controlDict` file and:

- replace the term `TFINAL` for the entry `endTime` with `5.0`
- replace the entry `DT` for the entry `deltaT` with `1e-3`
- replace the entry `PRECICE_FO`, a placeholder for the **preCICE Funtion Object** with the following:

```
    preCICE_Adapter
    {
        type preciceAdapterFunctionObject;
        libs ("libpreciceAdapterFunctionObject.so");
    }
```

Note: we are using the same $\Delta t$ for the **Fluid** and the **Solid** part, no subcycling.

Open the `preciceDict` file and:

- replace the entry `PATCH` in the `interface1` dictionary entry with the name given to the wing boundary patch (`naca2312`)
- replace the entry `RHO` in the `FSI` dictionary entry with the water density ($\rho_{water} = 1000.0 \frac{kg}{m^3}$)

## preCICE setup

Once we have prepared the **participants** we can setup **preCICE**.

Open the `precice-config.xml` file in the `skeleton` folder and:

- replace the **two** occurrencies of `RADIUS` in the `<mapping:rbf>` tag with  `0.05` (**TODO** motivate value?)
- in the `<watch-point>` tag replace:
  - `TIP_COORD` with `0.0;0.0;0.3`
  - `TIP_LE_COORD` with `-0.05;0.0;0.3`
  - `TIP_TE_COORD` with `0.05;0.0;0.3`
- replace `DT` in the `<time-window>` tag with `0.001`
- replace `TFINAL` in the `<max-time>` tag with `0.5`
- replace the **two** occurrencies of `REL_CONV` in the `<relative-convergence-measure>` tag with `1e-3`

**NOTES**:

- **TODO** RBF
- we are considering **3** watch-points at the tip of the wing, so that we can look at the displacement and at the pitching angle of the final section of the wing
- all the simulation components share the same $\Delta t$ and $t_{final}$
- **TODO** any notes on convergence

## Coupled simulation

Now you are ready to perform the coupled simulation:

### Solid participant

Open a terminal and enter the `Solid` folder. Here you simply run the `run_soilid.sh` script:

```
./run_solid.sh
```

### Fluid participant

Open another terminal and enter the `Fluid` folder. Here you have to:

- source OpenFOAM (e.g. type `of2406`)
- run `./Allrun.pre` which takes care of:
  - copying `0.orig` into `0`
  - executing `changeDictionary`
  - decomposing the case into **8** subdomains
- run `./run_fluid.sh` to start the parallel simulation

```
of2406
./Allrun.pre
./run_fluid.sh
```

### clean

In case you need to clean and restart your simulation, the utilities:

- `./Allclean` in the **Fluid** participant
- `./clean.sh` in the **Solid** participant

are provided.

## Monitoring

During the **FSI** simulation you can monitor the ongoing simulation through the following utilities:

- `./plotDisplacement.sh` which plots the **watch-points** displacements over time
- `python3 plotConvergence.py` which plots the number of iterations and the realative error for each time-step

## Results

Once you have finished your simulation you can have a look at the results.

### Fluid results

**TODO** clean from the 0.009 files. or we save each timestep

### Solid results

**TODO** convert from frd. we will obtain 500 files.

## Simulation 2 (optional)

**TODO**

- clean and rerun? copy? provide other case? point to "solution"?