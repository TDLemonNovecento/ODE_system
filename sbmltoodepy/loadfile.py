# rf: read file using sbmltoodepy package in python
# author: M. Stuke, 05-Sept-2021

# Conda env information:
# $ conda create --name lim_sbmltoodepy python=3
# $ conda activate lim_sbmltoodepy
# $ pip install sbmltoodepy

import sys
sys.path.insert(0, '../..') #add upstream folders for import

#get filename
import os
import var
import sbmltoodepy
import codecs

### DO NOT CHANGE! connected to loader function
os.getcwd()
modelfile = os.getcwd() + "/modelfile.py"

print("save modelfile to ", modelfile)

def filefixer(pymodelfile, filepath_new = None): #requires .py ending!
    #repare broken model with invalid signs
    if goodfile == None:
        goodfile = modelfile

    f = codecs.open(pymodelfile)
    contents = f.read()
    newcontents = contents.replace("·", ".")
    newcontents = newcontents.replace("nan", "1")
    f.close()

    f = open(goodfile, "w")
    f.write(newcontents)
    f.close()

    return(goodfile)


def errorcheck(filepath):
    #prints errors in file to console and returns True if file has no errors
    print("no errorcheck defined")
    return(True)

def loader(filepath):
    # create model in current folder in newsbmlmodel.py file
    os.getpwd()
    sbmltoodepy.ParseAndCreateModel(filepath,\
        outputFilePath = modfile, className = "SBMLmodel")    
    from modfile import SBMLmodel
    model = SBMLmodel()
    return(model)
