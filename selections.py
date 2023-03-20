# Working with selections in FEFLOW is part of the daily operations. Selections are used to store valuable information from the FEFLOW mesh. 
# Typical examples of selections are locations of a well (node selection), a specific region to be used for the flow calibration (element selection), a group of pipes/drainage (edge selection) and a complex fault system (face selection).
# FEFLOW Python Interface supports multiple methods to read, create and interact with selections:
# Create new selections and/or delete existing selections
# Find a selection with a given name and type
# Get all the items of an existing selection
# Evaluate whether a single item is within an existing selection
# FEFLOW selections can be of several topologies, thus the selection functions within the programming interface would require to know the type of selection. 
# The IFM constants in the FEFLOW Python interface are given in the table below:

# Selection Type	Python Constant Name
# Nodes	Enum.SEL_NODES
# Elements	Enum.SEL_ELEMS
# Edges	Enum.SEL_EDGES
# Faces	Enum.SEL_FACES
# Fractures (DFEs)	Enum.SEL_FRACS

# Objectives
# You will learn how to use FEFLOW Python methods to extract all the items of an existing selection using the selection name and type. 

# Example
# The script below opens a FEM document, read a nodal selection stored under the name "Wells" and pass all the items (IDs) to the Python variable "sel_items". 
# Subsequently, the information is print in the console.
# You will notice below that beside the standard FEFLOW Python import (first line import ifm), the script also imports the sub-package named Enum. 
# This FEFLOW package contains the list of all the IFM / Python constants.

import ifm
from ifm import Enum

FEM = r'..\femdata\box_wells.fem'
doc = ifm.loadDocument(FEM)
selName = 'Wells'
sel_items = doc.getSelectionItems(Enum.SEL_NODES, selName)
print(sel_items)
