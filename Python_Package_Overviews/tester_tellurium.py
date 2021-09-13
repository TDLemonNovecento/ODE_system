# M. Stuke, 27.08.2021
import logging # debug, info, warning, error, critical

# use simplesbml to open files
import tellurium as te
import var

import matplotlib
matplotlib.use('TkAgg') # to make matplotlib GUI backend


#logging.basicConfig(filename='Debug_Infos/tellurium_debug.log', level=logging.DEBUG)

try:
    print("hello")
    model = te.loadSBMLModel("C:/Users/Miriam/Documents/Miriam/Arbeit/Lim/part1_MATLAB_Assessment/Matlab_SBML/20210403-StickyPore_c_rangap-sequence_with_ImpB.sbml")
except:
    #logging.warning("an error has occured during the loading of the model")
    print("an Error occured")

#logging.debug('File %s was opened' % var.sl_filename)
#logging.info('Model Info:\n no_compartments: %s \n no_species: %s \n no_reactions:  %s' \
#    %(model.getNumCompartments(), model.getNumSpecies(), model.getNumReactions()))
m = model.simulate(start = 0, end = 20, points = 100)
model.plot()
print('end of executable file reached')
