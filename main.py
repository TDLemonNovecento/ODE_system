# fix report for use in tellurium
# Author: M. Stuke, 08-Sept-2021

import sys
sys.path.insert(0, '..') #add upstream folders for import

import var
#import setIdFromNames as idfix

## SET FILEPATHS
#filepath = var.sbml_filename
new_filepath = var.sbml_cleanfile
filepath = new_filepath #for fixed files
print("sbml file is being imported from:\n", filepath)

## SET METHOD
method = "tellurium" # or sbmltoode, ect (see available folders)

## SET SIMULATION SETTINGS
start = 0
end = 12000
points = 10000 #does not work with tellurium

# SET FLAGS FOR THIS RUN
CHECKFILE = True
FIXFILE = False
SAVE_NEWFILE = True
IMPORTFILE = True
SEE_SIMSETTINGS = False
CHANGE_SIMSETTINGS = False
RUN_SIMULATION = True
EXPORT_SIMRESULTS = False
GETODES = False
# Plotting requires import of specified plotting procedure
# Add as many as you like at end of file

IMPORT_FLAG = False # raised as false if file contains errors

#set some things straight:
if CHECKFILE and IMPORTFILE:
    FIXFILE = True

if SAVE_NEWFILE:
    print("sbml file is being saved after changes to:\n", new_filepath)


### Import method specific functions, start run
sys.path.insert(0, method) #add folders for import
from loadfile import errorcheck, filefixer, loader, getodes  #should import method specific filefixer
from runsimulation import simsettings, simchanger, simulator
from plotfile import *


if CHECKFILE:
    if errorcheck(filepath):
        print("your file has no errors")
        FIXFILE = False
    else:
        print("your file contains errors\n import of file prohibited without fix")
        IMPORT_FLAG = True


if FIXFILE:
    new_filepath = filefixer(filepath, new_filepath)
    if errorcheck(new_filepath):
        good_filepath = new_filepath
        IMPORT_FLAG = False
    else:
        print("your file contains errors after fixing")
        IMPORT_FLAG = True
    
if IMPORTFILE:
    if not IMPORT_FLAG:
        model = loader(filepath)
        print("model of type" , type(model), "was successfully imported")
    else:
       print("model could not be imported, system exiting")
       sys.exit()

    if SEE_SIMSETTINGS:
       print("current simulation settings")
       simsettings(model)

    if CHANGE_SIMSETTINGS:
       # get user input for new settings?
       from new_simsettings import simsettings
       simchanger(model, simsettings)

    if RUN_SIMULATION:
        results = simulator(model, end)
        print(results.colnames)
        if EXPORT_SIMRESULTS:
           save(results, resultspath)

if GETODES:
    print("\n######\n### These are the ODE's of the Model\n")
    print(getodes(model))

plotImpB_loners(model, end = end, steps = points)
plotImpB_GTP(model, end= end, steps = points)
