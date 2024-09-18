#import logging
import ccx2paraview.ccx2paraview as ccx2p

name = './dynamicModel.frd'

#logging.basicConfig(level=logging.INFO, format="%(levelname)s: %/message)s")
c = ccx2p.Converter(name, ["vtu"])
c.run()

