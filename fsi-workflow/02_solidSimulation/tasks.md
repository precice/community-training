# Task 2: simulation of the Solid domain

In this section we'll simulate the *Solid Domain* alone, to gain confidence with the **CalculiX** syntax and to check that our solid mesh and model work.

## Static Simulation

This model allows you to perform a static simulation in which the cantilevered wing is subjet to its own weight.

### Complete the staticModel.inp file

Enter the `static` folder and:

- Copy your generated solid mesh in the current folder

Open the `staticModel.inp` file and:

- replace **YOURMESH.inp** (line **4**) with the name of your mesh (`wing2312_m.inp`)
- replace **E**, **NU**, **RHO** (i.e. the material properties of the material, lines **10, 12**) with the following:
  - `2000000` ($E=2 GPa$)
  - `0.3` ($\nu = 0.3$)
  - `3000` ($\rho = 3000 \frac{kg}{m^3}$)
- replace **NODESET** (line **27**) with the name of the set of root nodes (`root_Nodes`)

Notice the structure of the file:

- lines **20-21**: define a linear static simulation, with a single computational step
- lines **31-32**: define a *distributed load* (body force) **GRAV** $\vec{g} = 9.81$ with direction $(0, -1, 0)$
- lines **36-39**: define the simulation output for each mesh element:
  - `U`: displacements
  - `S`: stresses
  - `E`: strains
- lines **43-44**: compute the resultants of the reaction forces `RF` on the root nodes.

### Run the simulation

In order to run the simulation, open a terminal in the current folder and type:

`ccx_preCICE -i staticModel`

**Notes**:

- remeber to type the input file without the extension
- if you need to clean your simulation, you can use `clean.sh`

### Analyze the results

The main result files are:

- `staticModel.frd`: which contains all the `U`, `S` and `E` information
- `staticModel.dat`: which contains the reaction force resultants

Geometric data:

- Area section of the wing: $A=8.0958 \cdot 10^{-4}m^2$
- length of the wing: $l=0.3m$

Compare the results in `staticModel.dat` with the expected reaction force (the total weight of the wing is $\rho \cdot g \cdot A \cdot l$)

(**TODO**: define how to open the frd file, remember FreeCAD scaling problems)

Compare the tip displacement in `staticModel.frd` with the expected result: 

$y_B = \frac{w l^4}{8EJ_x}$

![tip displacement](./images/cantilever.png)

Where:

- $w=\rho \cdot g \cdot A$: distributed load along the span
- $J_x = 6.9464 \cdot 10^{-9}m^4$

**NOTE**: we are a bit lazy here, as the $x, y$ axes are not *principal axes*, nevertheless we are very close and the approximation holds.

## Dynamic Simulation

This model allows you to perform a static simulation in which the cantilevered wing is subjet to its own weight.

### Complete the .inp file

Enter the `dynamic` folder and:

- Copy your generated solid mesh in the current folder

Open the `dynamicModel.inp` file and:

- replace **YOURMESH.inp** (line **4**) with the name of your mesh (`wing2312_m.inp`)
- replace **DAMP**, **DT**, **TFINAL** (lines **21, 22**) with the following:
  - `-0.05` (numerical damping, see notes below)
  - `1.E-2` ($\Delta  t = 1 \cdot 10^{-2}s$)
  - `2.` ($t_{final} = 2 s$)
- replace **NODESET** (line **27**) with the name of the set of root nodes (`root_Nodes`)
- replace **RAMPSEQUENCE** (line **32**) with the sequence `0.0, 0.05, 0.5, 1.0, 2.0, 1.0`, that is a sequence of values **time**, **amplitude** as in the following picture:  

![amplitude](./images/ampl.png)

Notice in the file:

- **DIRECT** specifies that the user-defined initial time increment should not be changed
- **ALPHA** takes an argument in the range $\left[-\frac{1}{3}, 0 \right]$. It controls the dissipation of the high frequency response: lower numbers lead to increased numerical damping
- lines **36-37**: define a *distributed load* (body force) **GRAV** $\vec{g} = 9.81$ with direction $(0, -1, 0)$ as we did in static simulation, but e are applying it with a factor defined in lines **31-32**.

### Run the dynamic simulation

In order to run the simulation, open a terminal in the current folder and type:

`ccx_preCICE -i dynamicModel`

**Notes**:

- remeber to type the input file without the extension
- if you need to clean your simulation, you can use `clean.sh`

### Analyze the dynamic results

The main result files are:

- `dynamicModel.frd`: which contains all the `U`, `S` and `E` information
- `dynamicModel.dat`: which contains the reaction force resultants

(**TODO**: read files, convert to VTU)

## References

CalculiX user manual: https://www.dhondt.de/ccx_2.20.pdf
Web version (possibly outdated): https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/ccx.html
