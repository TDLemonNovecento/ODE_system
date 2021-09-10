# rf: read file using tellurium package in python
# author: M. Stuke, 08-Sept-2021

# Conda env information:
# $ conda create --name lim_tellurium python=3
# $ conda activate lim_tellurium
# $ pip install tellurium
# $ pip install sbmlutils

import sys
#sys.path.insert(0, '../..') #add upstream folders for import

#get filename
import tellurium as te


def simsettings(model):
    #returns current simulation settings
    print("get current antimony:")
    str_antimony = model.getCurrentAntimony()
    print(str_antimony)
    return()

def simchanger(model, newsettings ):
    #newsettings as tuple?
    updated_model = model
    return(updated_model)

def simulator(model, end = 20):
    # runs simulation
    start = 0 #change here if desired other
    m = model.simulate(start = start, end = end)
    return(m)

def save(results, resultfile = "out_simresults.py"):
    # saves results into python file
    return(resultfile)
