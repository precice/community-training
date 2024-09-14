# Task 5: FSI simulation

Finally we are able to put everything together and start our **fluid-structure interaction** simulation. We'll use all the work done until now to setup our **Fluid** and **Solid** participants. The starting point of our case is in the `skeleton` folder, which is the root of our FSI case.

## Solid setup

Enter the `Solid` folder.

You need to use the mesh generated in step `01_solidMesh`: copy the `.inp` mesh in the current directory.

**NOTE**: Remember to use the one converted in *meters*.

### `solidModel.inp`

Check the following information in the file:

- section `*INCLUDE`: we are including the mesh named `wing2312_m.inp`, replace `with the actual name of your mesh, if different
- section `*MATERIAL`: the material properties correspond to a polymeric material close Polystyrene or ABS
- section `*DYNAMIC`: we perform a simulation $0.5$ seconds long with a time-step of $1ms$
- section `*BOUNDARY`: the group of the **root** (`Nroot_Nodes`) is fixed
- section `*AMPLITUDE`: we ramp the loading of the wing, starting with the $5\%$ of the total load, arriving at $100\%$ after $0.2s$

Complete the file with the following information:

- section `*CLOAD`: replace each of the `WETSURF` entries with the name of the group given to the **wet surface** (`NwetSurface_Nodes`)

### `config.yaml`

This file contains the information required by the **CalculiX adapter** to connect to **preCICE**. The information here must match the information contained in the `precice-config.xml` file. See the [CalculiX adapter documentation](https://precice.org/adapter-calculix-config.html).

- entry `patch`: replace `WETSURF` with the name of the group given to the *wet surface* (see the mesh `.inp` file), **WITHOUT the N at the beginning** (`wetSurface_Nodes`)

The rest of the entries specify the path to the preCICE configuration file, the coupling mesh defined in the preCICE configuration file (`Solid-Mesh`, a nodes-based mesh), the read data (forces), and the write data (absolute displacements).

The **Solid participant** is now ready, and we can move to the **Fluid participant**.

## Fluid setup

Now go back to the root of the case and enter the `Fluid` folder. This is a usual `OpenFOAM` case that we have to configure. For the preCICE-specific parts, have a look at the [OpenFOAM adapter documentation](https://precice.org/adapter-openfoam-config.html).

### `constant` folder

In this folder, we need to:

- copy our previously generated mesh: copy the `polyMesh` folder from your `0.003` folder in `03_fluidMesh/skeleton` (or from the `constant` folder in `04_fluidSimulation/skeleton/Fluid`)
- open the `dynamicMeshDict` and replace `WETSURF` in the `displacementLaplacianCoeffs` dictionary entry with the name given to the wing patch (`naca2312`, specified in `constant/polyMesh/boundary`). This file configures a mesh motion solver (`displacementLaplacian`).

### `0.orig` folder

In this folder there is a new dictionary file `pointDisplacement`: this is required by the **meshMotionSolver**.

Copy here the files:

- `U`
- `p`
- `phi`

that you have saved in `04_fluidSimulation/skeleton/results/water/250`. By copying results from the converged state of the steady-state simulation into the `0.orig/` (and effectively `0/`) directory, we are initializing the fluid domain with our previous solution.

### update of `U` file

When we performed the fluid simulation, in the `U` file for the initial conditions, we defined the surface of the wing as `noSlip`. This boundary condition remains through all your simulation and it is the current BC in the `U` file that you copied. In **FSI** simulations, we need that the velocity is overwritten by preCICE, for which we need to use the `movingWallVelocity` BC. To avoid opening a large file to look for a boundary condition, we can use the utility `changeDictionary`:

- open the file `changeDictionaryDict` in the `system` folder
- in the `boundaryField` dictionary entry, look for `PATCH` and replace it with `naca2312` and the entry `TYPE` with `movingWallVelocity`. We will update the boundary condition before running the coupled simulation (file `Allrun.pre`).

### `system` folder

Open the `controlDict` file and:

- replace the term `TFINAL` for the entry `endTime` with `0.5` (**NOTE:** the end time does not matter, the adapter sets it automatically)
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

Similarly to the `config.yml` file that we edited for the CalculiX adapter, we also need to configure the OpenFOAM adapter. Open the `preciceDict` file and:

- replace the entry `PATCH` in the `Interface1` dictionary entry with the name given to the wing boundary patch (`naca2312`)
- replace the entry `RHO` in the `FSI` dictionary entry with the water density ($\rho_{water} = 1000.0 \frac{kg}{m^3}$) We are using an incompressible solver, so the adapter needs a density value to compute the forces.

Notice that, compared to the previous, steady-state flow simulation, we are now using the transient `pimpleFoam` solver.

## preCICE setup

Once we have prepared the **participants** we can setup **preCICE**.

Open the `precice-config.xml` file in the `skeleton` folder and:

- in the `<watch-point>` tag replace:
  - `TIP_COORD` with `0.0;0.0;0.3`
  - `TIP_LE_COORD` with `-0.05;0.0;0.3`
  - `TIP_TE_COORD` with `0.05;0.0;0.3`
- replace `DT` in the `<time-window>` tag with `0.001`
- replace `TFINAL` in the `<max-time>` tag with `0.5`
- replace the **two** occurrencies of `REL_CONV` in the `<relative-convergence-measure>` tag with `1e-3`

**NOTES**:

- we are considering **3** watch-points at the tip of the wing, so that we can look at the displacement and at the pitching angle of the final section of the wing
- all the simulation components share the same $\Delta t$ and $t_{final}$
- The convergence measure that we chose is a good compromise between accuracy and execution time

## Coupled simulation

Now we are ready to perform the coupled simulation:

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
  - executing `changeDictionary` to switch the boundary condition from `noSlip` to `movingWallVelocity`
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
