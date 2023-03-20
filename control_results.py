#Typically, you would like to save the model results in a FEFLOW DAC file. 
#The programming interface offers you the possibility to define the file format (Default binary = 0, ASCII base = 1) and the list of time steps. 
#In the example below, the Python list [10, 20, 30] defines the simulation times (in days) to be added to the FEFLOW DAC file. 
#This is the same functionality available through the Record option in the FEFLOW GUI. 
#The method doc.saveDocument() with the target file name can be used to save a new FEFLOW file (or overwrite an existing). 
#For example, you could run the simulation and then same the final results in a new FEM document, instead of using a DAC document.

import ifm
FEM_FILE = r'..\femdata\quadri.fem'
DAC_FILE = r'..\results\quadri_test.dac'
doc = ifm.loadDocument(FEM_FILE)
doc.startSimulator(DAC_FILE, 0, [10, 20, 30])
doc.stopSimulator()
