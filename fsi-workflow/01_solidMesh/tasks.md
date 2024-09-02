# Task 1: Mesh of Solid domain

In this section we'll generate a CalculiX mesh for the solid, using FreeCAD.

## Adjust the FreeCAD settings

### Export settings

Before you start, change the settings of the INP exporter to export groups together with the mesh.

Select the `FEM Workbench`:

![FreeCAD: FEM Workbench](./images/FEM_WB.png)

Go to:

- Click `Edit` -> `Preferences...`.
- Select the `Import-Export` icon on the left.
- Select the `INP` tab.

Configure as follows:

- Which elements to export `All`.
- Export group data: (check).

Then, click `Apply` and `OK`.

### Temporary directories (optional)

Depending on the installation method (e.g., when using an AppImage file on Linux), some tools (e.g., GMSH) might not be able to write some necessary temporary files in the default directories. To ensure everything will go smooth (and to be able to explore what the tools do):

- Click `Edit` -> `Preferences`.
- Select the `FEM` icon from on the left.
- In the `General` tab, switch from `Temporary directories` to `Use custom directory`.
- Select a path where you know your user can write files (e.g., your `Desktop`).

## Import the wing

The first task consists in importing the wing:

- Create a new project: Click `File` -> `New`.
- Give the model a name: In the `Combo View/Model` tab on the left, select the unnamed model and change the `Label`: click on the `Unnamed` and rename it to `Wing`.

![FreeCAD: Rename model label](./images/PD_rename.png)

- Select the `Part design` workbench from the drop-down menu and click `create body`:

![FreeCAD: Create a new body from the Part design workbench](./images/PD_new.png)

- You can now see a new body as part of the `Wing` model:

![FreeCAD: Create a body](./images/PD_body.png)

- Click `File` -> `Import...`.
- Select the STEP file `naca2312.step`.

![FreeCAD: Import geometry](./images/PD_import.png)

An object named `Open CASCADE STEP Translator 7.5 1` should appear on the left and you should see the wing. Drag and drop this object into `Body`. This should appear as a `BaseFeature` entry under the `Body`.

![FreeCAD: BaseFeature](./images/PD_BF.png)

## Generate the mesh

Now we can generate a mesh for the `Wing`.

- Switch again to the FEM Workbench from the drop-down menu.
- From the menu bar, click `Model` -> `Analysis container` (or select the `A` symbol from the toolbar):

![FreeCAD: Analysis container](./images/FEM_Analysis.png)

- We want to mesh the `BaseFeature`: Select it from the sidebar.
- From the menu bar, click `Mesh` -> `FEM Mesh from shape by GMSH`. The FEM Workbench can generate meshes using different backends; we use [GMSH](https://gmsh.info/) here.

![FreeCAD: Add Analysis container](./images/FEM_Mesh01.png)

- Use the following parameters:
  - Element dimension: `3D`
  - Element order: `2nd`
  - Max element size: `20mm`
  - Min element size: `10mm`

![FreeCAD: GMSH parameters](./images/FEM_Mesh02.png)

- Click `Apply` and `OK` to generate the mesh.

If everything went as expected, a mesh should appear. In case you get any error related to creating temporary files, see the settings steps in the first section.

![FreeCAD: Mesh generated](./images/FEM_Mesh03.png)

## Create mesh groups

Now that we have a mesh, we also need to create the boundaries. We will need to identify the `root surface`, which will be clamped, and the `wet surface`, which will be in contact with the fluid. These surfaces are defined as `mesh groups`.

- From the `Model` tab, expand the `Analysis` branch and select `FEMMeshGmsh`:

![FreeCAD: Select FEMMeshGmsh](./images/Groups01.png)

- Click `Mesh` -> `FEM Mesh group`:

![FreeCAD: Mesh group](./images/Groups02.png)

  In case you cannot select anything and you get an error "Active Task Dialog found!", you might need to switch to the `Tasks` tab and click `OK` or `Cancel` to exit from the previous task.

- In the `Model` tab, there should now also be a `MeshGroup` under the `FEMMeshGmsh`.

![FreeCAD: Added MeshGroup](./images/Groups03.png)

- In the `Tasks` tab, select `Label` as `Identifier used for mesh export` and `Face, Edge, Vertex` as `Selection mode`:

![FreeCAD: Add surface to mesh group](./images/Groups04.png)

- Click `Add`, then click on the rendering to select the profile of the wing (pay attention to reference frame to identify it), and `OK` to add the surface to the mesh group. You can rotate the view using the cube on the upper right corner, or [using your mouse](https://wiki.freecad.org/Mouse_navigation) (e.g., by `Shift` + `right click`).

![FreeCAD: surface group for root](./images/root_Group.png)

- In the `Model` tab, select the `MeshGroup` and rename its `Label` to `root`. This will help us define the boundary condition in the Solid domain.

![FreeCAD: Rename mesh group](./images/Groups05.png)

- Define a new group comprising all components of the `wetSurface` (they are 4: as shown below. Pay attention to the trailing edge surface, you need to zoom-in to see it). Remember to first select `FEMMeshGmsh`.

| ![FreeCAD: wet surface 1](./images/group_WS_01.png) | ![FreeCAD: wet surface 2](./images/group_WS_02.png) |
| ![FreeCAD: wet surface 3](./images/group_WS_03.png) | ![FreeCAD: wet surface 4](./images/group_WS_04.png) |

- In order to define a goup with multiple surfaces:
  1. click `Add`
  2. `select` the desired surface 
  3. `repeat` steps `1.` and `2.` for each of the four elements
  4. Click `OK` 

![FreeCAD: wet surface steps](./images/group_WS_steps.png)  
  
- As for the `root` Group. change the `Label` in the `Properties` to `wetSurface`

![FreeCAD: Rename wet surface group](./images/group_WS_rename.png)

- Finally, create a group for the wingtip surface using the same steps used for the root surface, with group name `lowerSurface`. It will be used for single physics tests.

![FreeCAD: lower surface group](./images/lowerSurf_Group.png)

You should come up with a list of three groups under the current mesh.

![FreeCAD: final list of groups](./images/groups_final_LS.png)

Select the mesh (`FEMMeshGmsh`) -> double click -> click `Apply` to remesh and create groups -> click `OK`.

**IMPORTANT**: You need to remesh, otherwise the groups won't be created.

## Export the mesh file and verify

- Keep the mesh selected.
- Click `File` -> `Export...`.
- Name the file  `wing2312.inp`.
- Select `FEM mesh formats (*.dat, *.inp, ...)`.
- Click `Save`.

Save also the FreeCAD model with `File` -> `Save`.

To verify, open the `wing2312.inp` file you just generated with a text editor:

- Look for `NSET`: you should find
  - `NSET=Nall`: this keyword defines the beginning of the list of coordinates of all the mesh nodes
  - `*NSET, NSET=root_Nodes`: this keyword defines the beginning of the list of node IDs belonging to the mesh group `root`
  - `*NSET, NSET=wetSurface_Nodes`: this keyword defines the beginning of the list of node IDs belonging to the mesh group `wetSurface`
  - `*NSET, NSET=lowerSurface_Nodes`: this keyword defines the beginning of the list of node IDs belonging to the mesh group `lowerSurface`  
- Take note of the exact names of all the sets of nodes for each of the groups, because we'll use them in the following steps.
- `*ELSET, ELSET=GROUPNAME_Faces`: where `GROUPNAME` is one of the groups that you defined (`root`, `wetSurface`, `lowerSurface`). These sets define the groups of surface elements. We don't need them for the FSI simulation
- save and close

## Scale the mesh file

Unfortunately, **FreeCAD** exports all node coordinates in **mm** and there is no option to change it. We prefer to have everything in **SI** units so, in the `10_utils` folder you can find a `inp_convert.py` file. Copy it in your folder and, after checking that the name on line **43** matches your mesh file, run it:

`python3 inp_convert.py`

You should find a `wing2312_m.inp` file in your folder.
