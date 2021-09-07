# rf: read file using tellurium package in python
# author: M. Stuke, 05-Sept-2021

# Conda env information:
# $ conda create --name lim_tellurium python=3
# $ conda activate lim_tellurium
# $ pip install tellurium
# $ pip install sbmlutils

import sys
sys.path.insert(0, '../..') #add upstream folders for import

#get filename
import var
print("sbml file is being imported from:\n", var.sblm_filename)

import tellurium as te
from sbmlutils.io import read_sbml #for error checking
from sbmlutils.validation import validate_doc

#import model
print("tellurium crashes when model has errors, therefore check for errors with following method:")

def errorcheck(filepath):
    model = read_sbml(var.sblm_filename); # import model to sbmlutils
    p = validate_doc(model, units_consistency=False); # validate model 
    return(p.is_valid())


print("errorcheck of file:", errorcheck(var.sblm_filename))
if errorcheck(var.sblm_filename):
    model = te.loadSBMLModel(var.sblm_filename)
else:
    print("the model has errors, please use sbmlutils to find out where")


