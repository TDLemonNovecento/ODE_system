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
    return(model)

def simchanger(model, newsettings ):
    #newsettings as tuple?
    updated_model = model
    return(updated_model)

def simulator(model, start = 0, end = 20, points = 100):
    # runs simulation
    m = model.simulate(start = start, end = end, points = points)
