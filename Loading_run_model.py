#With the following Python lines, you can open an existing FEFLOW document and start the simulator. The script is completed after the simulation is done.
#The FEFLOW Python interface is initialised with the first line, after importing the FEFLOW package ifm. 
#Every script requires to create a document object (doc), which corresponds to either a FEFLOW FEM file or a FEFLOW Result DAC file. 
#Multiple documents can be opened within the same script.

#The DHI License Manager makes the license check at ifm.loadDocument(). 
#If the license check passes successfully, the script moves to the next line and the simulation starts with doc.startSimulator(). 
#The method doc.stopSimulator() forces the script to leave the Simulation mode. You can review all other kernel methods in the online help (here).

import ifm
FEM_FILE = r'..\femdata\quadri.fem'
doc = ifm.loadDocument(FEM_FILE)
doc.startSimulator()
doc.stopSimulator()
