#import logging
import ccx2paraview.ccx2paraview as ccx2p
import os
import shutil

name = './solidModel.frd'

#logging.basicConfig(level=logging.INFO, format="%(levelname)s: %/message)s")
c = ccx2p.Converter(name, ["vtu"])
c.run()

destination_folder = './convert'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created folder: {destination_folder}")
    
# Get the list of files in the source folder
files = os.listdir('./')
    
# Loop through the files and copy the ones with the specified extension
for file in files:
    if file.endswith('.vtu') or file.endswith('.pvd'):
        full_file_path = os.path.join(os.path.abspath('./'), file)
        shutil.move(full_file_path, os.path.abspath(destination_folder))
        print(f"Moved {file} to {destination_folder}")
