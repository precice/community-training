# Step 4: simulation of the Fluid domain

In this section we'll use the previously generated Fluid Mesh to perform a single physics simulation.
This will allow us to perform two important tasks:

- check the validity of our model
- obtain an initialized fluid domain, to be used in the FSI simulation

## Introduction

We want an initialized fluid domain, so we can simply perform a **steady state** simulation.

You'll find the required files in the `skeleton` directory. The `Fluid` directory is the OpenFOAM root case, containing the `constant`, `system` and
`0.orig` folders. We put everything into the `Fluid` directory to familiarize with the fact that we'll soon have a `Fluid` and a `Solid` case.

**TODO** decide how to proceed:

- one case:
    1. $Re=5\cdot 10^4$ laminar, incompressible, water (tested)
    2. $Re=2\cdot 10^5$ laminar, incompressible, air (tested)
    3. $Re \geq 2\cdot 10^5$ *turbulent*, incompressible, air (crashes, to be improved)
    4. $Re \geq 1\cdot 10^6$ *turbulent*, *compressible*, air (to be prepared)
- two cases:
    1. case **1** and **2** above
    2. other combination

## Setup *Simulation 1*

Here we consider a laminar incompressible simulation in water. The main parameters are:

- $U_{\infty} = 0.5$
- $\rho = 1000$
- $\nu = 1 \cdot 10^{-6}$
- $Re = \frac{U_{\infty} c}{\nu} = 5 \cdot 10^4$

### `0.orig` folder

This folder contains the initial conditions for each of the simulation variables: files `U` and `p` (plus other files in case you want to set up a turbulent model).

Open the file `U` and:

- substitute **UINF** at line 19 with the value **0.5**. This initializes the whole domain to $U_{\infty}$
- substitute the boundary condition **BOUNDARY** for the *naca2312* patch at line **28** with **noSlip**

Note: we use the folder `0.orig` instead of the usual folder `0` just in case the simulation overwrites the initial conditions (e.g. you perform `potentialFoam` to initialize the fluid domain). The launch script that we prepared will take care of copying `0.orig` to `0`.

### `constant` folder

Here you need to perform the following activities:

- Use the **mesh** you generated in the previous task: copy the `polyMesh` folder, that you find in the `0.003` folder, in here
- Open the `transportProperties` file to define the kinematic viscosity $\nu$: substitute **NU** at line **19** with `1e-06`
- Open the `turbulenceProperties` file to define the type of simulation: uncomment line **17** to perform a **laminar** simulation

### `system` folder

Here you will define how many simulation steps you want to perform and you will make use of *function objects* in order to compute **forces, moments** and **force** and **moment coefficients**:

- Open the `controlDict` file and:
    1. substitute **END** with **250** at line **26**: we will perform 250 simulation steps at most
    2. substitute **RHO** with **1000.0** at lines **77** and **102**
    3. substitute **UINF** with **0.5** at line **111**
    4. substitute **CHORD** with **0.1**at line **112**
    5. substitute **AREA** with **0.03** at line **113**

Then you will define the type of the simulation and some thresholds for the residuals so that, if we reach those values, the simulation stops before *endTime*:

- Open `fvSchemes` and substitute **SIMULATIONTYPE** with **steadyState**
- Open `fvSchemes` and:
    1. substitute **P_RES** with **1e-4** at line **96**
    2. substitute **U_RES** with **1e-5** at line **97**

## Run the case

In order to run simulation, open a terminal from the `skeleton` folder, source OpenFOAM (e.g. type `of2406`) and then type `./run_case.sh`. This script will take care of:

- copying `0.orig` into `0`
- decomposing the case
- running `simpleFoam` in parallel and logging the output in `log.solver`
- reconstucting the latest timeStep

## Monitoring

(**TODO** check if available)

To check the simulation progress and plot the residuals over time, you can:

- open another terminal
- go to the `Fluid` folder
- source OpenFOAM
- type `pyFoamPlotWatcher log.solver`

## Analysis of the results

**TODO** comparison to "expected results"

- plot forces and force coefficients over time?
- compute theoretical $C_D$ $C_L$?

## Setup *Simulation 2*

Now we consider a laminar incompressible simulation in air. The main parameters are:

- $U_{\infty} = 30$
- $\rho = 1.225$
- $\nu = 1.5 \cdot 10^{-5}$
- $Re = \frac{U_{\infty} c}{\nu} = 2 \cdot 10^5$

We have to

- use `clean_case.sh` (**TODO** explain what it does)
- move the 250 directory somewhere, to use it in the FSI
- update the simulation values with the values above plus **endTime = 200**
- rerun simulation


Other **TODOS**:

- decide whether to keep k, omega, nut and the ods file or delete them