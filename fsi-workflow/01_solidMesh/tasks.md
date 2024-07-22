# FSI Workflow

A training module showcasing how to setup an FSI simulation from scratch.


---


Tasks:

 - [ ] **Geometry** preparation
 - [x] Meshing of **Solid Domain**
 - [ ] Meshing of **Fluid Domain** 
 - [ ] etc. [TODO: update]
 
 

 ---
 
 # Step 1: Mesh of Solid domain
 
 In this section we'll generate the **Solid Mesh** using **FreeCAD** version *0.21.2*.
 
 
 ## Configuration Check 
 
 
 ==please note== : if you are using the **usb live** [TODO: update name] you can safely skip this task.
 
 Before you start, please perform the following check:
 
 Select the **FEM Workbench**
 
 ![FEM Workbench](./images/FEM_WB.png)
 
 
 Go to:
 
 - Edit->Preferences
 - select the *Import-Export* icon to the left
 - select the **INP** tab

Configure as follows:

- Which elements to export **FEM**
- Export group data:  :heavy_check_mark:

Then:

 - press **Apply**
 - press **Ok** 

This allows us to export all the groups together with the mesh.
 
 
 ## Import the wing
 
 The first task consists in importing the wing:
 
 - File->New
 - (optional) in the **model** tab in **combo view** on the left: select *Unnamed* and rename it to *wing* in label property
 
 ![rename](./images/PD_rename.png)
 
 - (drop down menu) Part design->create body (or press button)

 ![rename](./images/PD_new.png)
 
 - You'll find a new **body** in the *combo view*
 
 ![rename](./images/PD_body.png)
 

 - File->import
 - Select step file **naca2312.step**

 ![rename](./images/PD_import.png)


An object named *Open CASCADE STEP Translator 7.5 1* should appear on the left and you should see the wing.

Drag and drop "Open CASCADE STEP Translator 7.5 1" into Body -> **BaseFeature** Appears

![BaseFeature](./images/PD_BF.png)

## Mesh the wing

Now we mesh the wing:

 - (drop down menu) FEM
 - Model->Analysis container (or press button A)

![Analysis](./images/FEM_Analysis.png)
 
- select BaseFeature 
- Mesh-> FEM Mesh from shape by GMSH

![Analysis](./images/FEM_Mesh01.png)

 - Use the following parameters:
     - Element dimension **3D**
     - Element order **2nd**
     - Max **20mm**
     - Min **10mm** 

![parameters](./images/FEM_Mesh02.png)


 - press **Apply**
 - press **Ok**


**Body is meshed**

![Analysis](./images/FEM_Mesh03.png)


## Create groups

- select *FEMMeshGmsh*

![select](./images/Groups01.png)

 - Mesh->FEM Mesh group
 
![select](./images/Groups02.png)

 - Make sure that the **BaseFeature** geometry is visible
 
![select](./images/Groups03.png)
 
 - check Label in the *Tasks* tab of *Combo module** on the left
 
![select](./images/Groups04.png)
 
 - click **Add** and select *root surface* (pay attention to reference frame to identify it) ->Add ->Ok
 - rename Label in Properties to **root**

![select](./images/Groups05.png)

 - repeat for other surfaces (they are **4**: upper, lower, tip and trailing. pay attention to trailing edge surface)
 - rename the group to **wetSurface**

 - repeat for tip surface (it will be used for single physics test)
 - rename the group to **tip**

Select the mesh->double click-> press apply to remesh and create groups-> ok

==IMPORTANT==: you need to remesh otherwise the groups won't be created

## Save INP file and verify

 - keep the mesh selected
 - File->export 
 - name the file  **wing2312.inp**
 - save
 - close
 - File->Save the FreeCAD model

open the **inp** file with a text editor:


 - look for **ELSET**, skip Evolume, you may remove remove all other ELSET
 - look for **NSET**, skip Nall
     - *NSET, NSET=tip_Nodes 
     - *NSET, NSET=wetSurface_Nodes
     - *NSET, NSET=root_Nodes
- Notice the names of all the sets of nodes for each of the groups.
- save and close

 ---
 
 ## Notes [TLDR]
 
 
 ---
 
 ## References
 
 ```
Edit->Preferences
```
