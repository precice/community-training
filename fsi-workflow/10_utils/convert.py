import logging
import ccx2paraview.ccx2paraview as ccx2p

name = '../03_solidSimulation/solution/staticModel.frd'

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %/message)s")
c = ccx2p.Converter(name, ["vtk"])
c.run()

