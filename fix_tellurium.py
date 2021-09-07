# fix report for use in tellurium
# Author: M. Stuke, 06-Sept-2021

import sys
sys.path.insert(0, '..') #add upstream folders for import


import fixer_sbmlreports as fix
import var
import subprocess
import setIdFromNames as idfix

print("sbml file is being imported from:\n", var.sbml_filename)
print(var.sbml_filename[-5:])
#fix.errorcheck(var.sbml_filename)
new_ID = idfix()
new_ID.main(var.sbml_filename,var.sbml_cleanfile)
