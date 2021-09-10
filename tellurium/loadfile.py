# rf: read file using tellurium package in python
# author: M. Stuke, 05-Sept-2021

## Works for ../main.py

# Conda env information:
# $ conda create --name lim_tellurium python=3
# $ conda activate lim_tellurium
# $ pip install tellurium
# $ pip install sbmlutils

import sys
sys.path.insert(0, '../..') #add upstream folders for import

#get filename
import var
import tellurium as te
from sbmlutils.io import read_sbml #for error checking
from sbmlutils.validation import validate_doc
import setIdFromNames as idfix
import shutil

def errorcheck(filepath):
    #prints errors in file to console and returns True if file has no errors
    model = read_sbml(filepath); # import model to sbmlutils
    p = validate_doc(model, units_consistency=False); # validate model 
    return(p.is_valid())

def filefixer(filepath, filepath_new = var.sbml_cleanfile):
    # prints fixed model to new filepath
    if errorcheck(filepath):
        print("file has no errors, copying to new filepath")
        shutil.copyfile(filepath, filepath_new)
        return(filepath_new)
    else:
        print("the model has errors, rewriting to var.sbml_cleanfile with exchanged names for id")
        idfix.main([None, filepath, filepath_new])
        print("errorcheck of new file at", filepath_new)
        if errorcheck(filepath_new):
            print("fixing successful")
            return(filepath_new)
        else:
            print("file still contains errors")
            return(None)

def loader(filepath, filepath_new = var.sbml_cleanfile):
    if errorcheck(filepath):
        model = te.loadSBMLModel(filepath_new) #uses roadrunner
    else:
        print("model could not be loaded with tellurium")
        model = None 
    
    return(model)

def getodes(model):
    return(te.getODEsFromModel(model))

