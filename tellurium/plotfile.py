# Author: M. Stuke, 10-Sept-2021

import re
import matplotlib.pyplot as plt
import numpy as np
import tellurium as te

def simpleplot(model, results, end=1000, steps=1000, filename = None):
    if filename == None:
        filename = "trialplot.png"
    model.plot(results)
    plt.savefig(filename)
    print("Simple plot was saved to", filename)
    return(filename)

def plotImpB_GTP(model, results):
    plt.xlabel("time [second]")
    plt.ylabel("GTP")
    
    cols_included = []
    for col in results.colnames:
        cols_included.append(bool(re.search('GTP', col)))
        if bool(re.search('GTP', col)):
            print(col, "is included")
    te.plotArray(results[:,cols_included])

    #model.plot(results[:,1]) #include only loners ["id_ImpB", "id_RanGAP", "id_RanBP1"]
    plt.savefig("myfile.png")

def plotImpB_loners(model, end = 1000, steps = 100):
    # set selections
    model.selections=['time', 'id_ImpB', 'id_RanGAP', 'id_RanBP1']
    model.integrator.setValue("variable_step_size", False)
    model.resetAll()
    r = model.simulate(0, end, steps)
    model.plot()
    plt.savefig("loners_trial.png")

def plotImpB_GTP(model, end = 10000, steps = 10000):
    r = model.simulate(0, end, steps, ['time', 'id_Ran_GTP', 'id_ImpB_Ran_GTP', 'id_ImpB_Ran_GTP_RanBP1', 'id_Ran_GTP_RanBP1'])
    model.plot()
    plt.legend({'Ran.GTP', 'ImpB.Ran.GTP', 'ImpB.Ran.GTP.RanBP1', 'Ran.GTP.Ran.BP1'});
    plt.savefig("GTP_trial.png")
