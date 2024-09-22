.PHONY: all

all:
	(cd 00_geometry && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task0.pdf)
	
	(cd 01_solidMesh && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task1.pdf)
	
	(cd 02_solidSimulation && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task2.pdf)
	
	(cd 03_fluidMesh && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task3.pdf)
	
	(cd 04_fluidSimulation && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task4.pdf)
	
	(cd 05_FSI && pandoc -V geometry:left=1in -V geometry:right=1in -V geometry:bottom=1.5in -V geometry:top=1in -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task5.pdf)
	
	pdfunite 00_geometry/task0.pdf 01_solidMesh/task1.pdf 02_solidSimulation/task2.pdf 03_fluidMesh/task3.pdf  04_fluidSimulation/task4.pdf 05_FSI/task5.pdf fsi-workflow-tasks.pdf
