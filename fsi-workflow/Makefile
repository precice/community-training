.PHONY: all

all: task0 task1 task2 task3 task4 task5
	
	pdfunite 00_geometry/task0.pdf 01_solidMesh/task1.pdf 02_solidSimulation/task2.pdf 03_fluidMesh/task3.pdf  04_fluidSimulation/task4.pdf 05_FSI/task5.pdf precice-course-fsi-workflow-tasks.pdf
	
task0: 00_geometry/tasks.md
	(cd 00_geometry && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task0.pdf)

task1: 01_solidMesh/tasks.md
	(cd 01_solidMesh && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task1.pdf)

task2: 02_solidSimulation/tasks.md
	(cd 02_solidSimulation && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task2.pdf)

task3: 03_fluidMesh/tasks.md
	(cd 03_fluidMesh && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task3.pdf)

task4: 04_fluidSimulation/tasks.md
	(cd 04_fluidSimulation && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task4.pdf)

task5: 05_FSI/tasks.md
	(cd 05_FSI && pandoc -V geometry:left=2.5cm -V geometry:right=2.5cm -V geometry:bottom=3.8cm -V geometry:top=2.5cm -V linkcolor:blue --filter pandoc-fignos -s tasks.md -o task5.pdf)

clean:
	rm -f 00_geometry/task0.pdf 01_solidMesh/task1.pdf 02_solidSimulation/task2.pdf 03_fluidMesh/task3.pdf 04_fluidSimulation/task4.pdf 05_FSI/task5.pdf precice-course-fsi-workflow-tasks.pdf

