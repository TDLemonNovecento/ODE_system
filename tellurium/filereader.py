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

import tellurium as te
from sbmlutils.io import read_sbml
from sbmlutils.validation import validate_doc

import translate_plotfile as tplot

import fixer_sbmlreports as fix
import var
import subprocess
import setIdFromNames as idfix



def fix_file(filename):
print("sbml file is being imported from:\n", var.sbml_filename)
fix.errorcheck(var.sbml_filename)
idfix.main([None, var.sbml_filename,var.sbml_cleanfile])


filepath = var.sbml_cleanfile
print("sbml file is being imported from:\n", filepath)

def errorcheck(filepath):
    model = read_sbml(filepath); # import model to sbmlutils
    p = validate_doc(model, units_consistency=False); # validate model
    return(p.is_valid())

print("errorcheck of file:")
ERROR_FREE = errorcheck(filepath)
if ERROR_FREE:
    model = te.loadSBMLModel(filepath)
else:
    print("the model has errors, please use fixfile.py to repare")
    sys.exit()

#continue doing simulation


#continue doing plotting
tplot.translate_and_save(var.mat_filename, var.plotfile)

print("reached end of file")

