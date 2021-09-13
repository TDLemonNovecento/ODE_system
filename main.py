# fix report for use in tellurium
# Author: M. Stuke, 08-Sept-2021

import sys

import var

## SET FILEPATHS
#filepath = var.sbml_filename
new_filepath = var.sbml_cleanfile
filepath = new_filepath #for fixed files
print("sbml file is being imported from:\n", filepath)

## SET METHOD
method = "tellurium" # or sbmltoode, ect (see available folders)

## SET SIMULATION SETTINGS
start = 0
end = 12
points = 17 #does not work with tellurium

# SET FLAGS FOR THIS RUN
CHECKFILE = False  # use sbmlutils to check conformity
FIXFILE = False  # set IDs from names
IMPORTFILE = True  # te.loadSBMLModel
SEE_SIMSETTINGS = True  # dict(model) or antimony format
CHANGE_SIMSETTINGS = True  # initial conditions from new_simsettings.py
RUN_SIMULATION = True  # get NamedArray
EXPORT_SIMRESULTS = False  # [not implemented]
GETODES = False  # te.getODEsFromModel
PLOT_EXAMPLE = True  # Plotting requires import of specified plotting procedure; cf. `simpleplot` from plotfile.py
# Add as many as you like at end of file

IMPORT_FLAG = False # raised as false if file contains errors

#set some things straight:
if CHECKFILE and IMPORTFILE:
    FIXFILE = True

    print("sbml file is being saved after changes to:\n", new_filepath)


### Import method specific functions, start run
sys.path.insert(0, method) #add folders for import
from loadfile import errorcheck, filefixer, loader, getodes  #should import method specific filefixer
from simfile import simsettings, simchanger, simulator
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
        params = simsettings(model)
        print("to change settings, add information on following data:")
        print(params)

    if CHANGE_SIMSETTINGS:
       # get user input for new settings?
       from new_simsettings import simsettings
       model = simsettings(model)

    if RUN_SIMULATION:
        results = simulator(model, end, points)
        #print(results.colnames)
        
        if EXPORT_SIMRESULTS:
           save(results, resultspath) #not running yet
        if PLOT_EXAMPLE:
            simpleplot(model, results, end = end, steps = points)  # can add filename


if GETODES:
    print("\n######\n### These are the ODE's of the Model\n")
    print(getodes(model))

## Add all desired plotting regimes below, examples given for tellurium

#plotImpB_loners(model, end = end, steps = points)
#plotImpB_GTP(model, end= end, steps = points)
