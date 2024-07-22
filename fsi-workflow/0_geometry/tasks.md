# FSI Workflow

A training module showcasing how to setup an FSI simulation from scratch.


---


Tasks:

 - [x] **Geometry** preparation
 - [ ] Meshing of **Solid Domain**
 - [ ] Meshing of **Fluid Domain** 
 - [ ] etc. [TODO: update]
 
 

 ---
 
 # Step 0: Geometry preparation
 
Our case involves a **NACA2312** profile wing with:

 - *chord* $c=100mm$
 - *span* $b=300mm$
 
 In this folder you already find the model of the wing that you'll be using during the rest of the training. Our training starts with *meshing*, but in real life you'll need to generate your geometry.
 You'll notice that two different file formats are provided **stl** and **step**. Both are widely used for data exchange and nearly all CAD systems allow to *import/export* such formats.
 
 We are considering an external flow, so we'll use the solid geometry to generate the **solid mesh** and we'll subtract it from a sufficiently large box to generate the **fluid mesh**.
 
 
 ---
 
 ## Notes [TLDR]
 
 
 You might wonder: "Why two formats?": **stl** (which describes an unstructured triangulated surface) is required if you want to mesh using `snappyHexMesh` in OpenFOAM. As it describes a *surface*, sometimes some tools fail to recognize a *solid* from it.
 For this reason, we'll use the *step* format, which is quite robust and explicitly defines volumes.
 
 Once you generate your model with your favorite CAD tool, you can export it in both formats and use them the way we'll use them in the following tasks.
 
 Notice that sometimes some parameters need to be tuned in order to obtain a sufficiently refined **stl** surface.
 
 
 ---
 
 ## References
 
 - [STL](https://en.wikipedia.org/wiki/STL_(file_format)) file format
 - [STEP](https://en.wikipedia.org/wiki/ISO_10303-21) file format 
 
 