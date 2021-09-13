# M.Stuke, 31.08.2021
import sbmltoodepy
import var
import os
import codecs
import matplotlib.pyplot as plt

os.getcwd()
tmp_pyfile = os.getcwd() + "\part2_Python\\test_sbml_to_odepy.py"
good_pyfile = os.getcwd() + "\part2_Python\\sbml_to_odepy.py"

def encode():
    f = codecs.open(tmp_pyfile)
    contents = f.read()
    newcontents = contents.replace("·", ".")
    newcontents = newcontents.replace("nan", "1")
    f.close()

    f = open(good_pyfile, "w")
    f.write(newcontents)
    f.close()


sbmltoodepy.ParseAndCreateModel(var.laptop_sblmpath,\
    outputFilePath = tmp_pyfile, className = "SBMLmodel")
#dataOfModel = sbmltoodepy.parse.ParseSBMLFile(var.laptop_sblmpath)
#sbmltoodepy.modulegeneration.GenerateModel(dataOfModel, tmp_pyfile, objectName = "SBML_Model")

# replace one special sign which causes errors
encode()

from sbml_to_odepy import SBMLmodel
modelInstance = SBMLmodel()
# get the dictionary keys for the IDs of the species in the model
#print(modelInstance.s.keys())
# get the dictionary keys for the IDs of the compartments in the model
#print(modelInstance.c.keys())
# get the dictionary keys for the IDs of the parameters in the model
print(modelInstance.p.keys())

print("time_0:", modelInstance.time)

timeinterval = 1
print(modelInstance.s['mwb63e16bc_62cb_4400_b88e_4bfde8a9f824'].concentration)

import numpy as np
times = np.zeros(101)
times[0] = modelInstance.time
concentrations = np.zeros(101)
concentrations[0] = modelInstance.s['mwb63e16bc_62cb_4400_b88e_4bfde8a9f824'].concentration
timeinterval = 1
for i in range(100):
	modelInstance.RunSimulation(timeinterval)
	times[i+1] = modelInstance.time
	concentrations[i+1] = modelInstance.s['mwb63e16bc_62cb_4400_b88e_4bfde8a9f824'].concentration

plt.plot(times,concentrations)
plt.show()

#plt.plot(sim)
#plt.savefig("trialplot.png")
