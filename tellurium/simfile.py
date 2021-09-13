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
    #returns current parameters that can be changed
    #print("get current antimony:")
    #str_antimony = model.getCurrentAntimony()
    #print(str_antimony) #if more information is desired
    return(dict(model))

def simchanger(model, newsettings ):
    #newsettings as tuple?
    #for param in te.ParameterScan(model):
    #    newp = input("Value of param ", param)
    #    print(model.param)
    updated_model = model
    return(updated_model)

def simulator(model, end = 20, steps = 1000):
    # runs simulation
    print(model.getInfo())
    model.integrator.initial_time_step = 0.00001
    start = 0 #change here if desired other
    print(model.__dict__)
    print(model.getInfo())
    m = model.simulate(start = start, end = end, steps = steps)
    return(m)

def save(results, resultfile = "out_simresults.py"):
    # saves results into python file
    return(resultfile)
