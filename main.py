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
end = 20
points = 100

# SET FLAGS FOR THIS RUN
CHECKFILE = True
FIXFILE = False
SAVE_NEWFILE = True
IMPORTFILE = True
CHANGE_SIMSETTINGS = True
RUN_SIMULATION = True
EXPORT_SIMRESULTS = True

IMPORT_FLAG = False # raised as false if file contains errors

#set some things straight:
if CHECKFILE and IMPORTFILE:
    FIXFILE = True

if SAVE_NEWFILE:
    print("sbml file is being saved after changes to:\n", new_filepath)


# start run
sys.path.insert(0, method) #add folders for import
from loadfile import errorcheck, filefixer, loader  #should import method specific filefixer
from runsimulation import simsettings, simchanger, simulator

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

    if CHANGE_SIMSETTINGS:
       print("current simulation settings")
       simsettings(model)
       # get user input for new settings?
       simchanger(model)

    if RUN_SIMULATION:
       results = simulator(model, start, end, points)
       if EXPORT_RESULTS:
           save(results, resultspath)

    
