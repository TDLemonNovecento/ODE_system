# M. Stuke, 27.08.2021
import logging # debug, info, warning, error, critical

# use sbmlutils to open files
from sbmlutils.io import read_sbml
from sbmlutils.validation import validate_doc

import var

#logging.basicConfig(filename='Debug_Infos/simplesbml_debug.log', level=logging.DEBUG)

# 1. open file
model = read_sbml(var.laptop_sblmpath)

print(model.getListOfAllElements())

# validate model
p = validate_doc(model, units_consistency=False);
print(p.is_valid)
#logging.debug('File %s was opened' % var.sl_filename)
