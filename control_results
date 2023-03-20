import ifm
FEM_FILE = r'..\femdata\quadri.fem'
DAC_FILE = r'..\results\quadri_test.dac'
doc = ifm.loadDocument(FEM_FILE)
doc.startSimulator(DAC_FILE, 0, [10, 20, 30])
doc.stopSimulator()
