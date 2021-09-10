import numpy as np

def simsettings(model):
    print(model.p.keys())
    return()

def runsimulation(model, start = 0, end, timesteps):
    print("time_0:", modelInstance.time)

    print(modelInstance.s[].concentration)

    times = np.zeros(timesteps+1)
    times[0] = model.time
    concentrations = np.zeros(timesteps+1)
    concentrations[0] = model.s[].concentration
    timeinterval = 1
    for i in range(timesteps):
	model.RunSimulation(timeinterval)
	times[i+1] = model.time
	concentrations[i+1] = model.s[].concentration

    return(times, concentrations)

def showsimulation(times, concentration):
    plt.plot(times, concentration)
    plt.show()
