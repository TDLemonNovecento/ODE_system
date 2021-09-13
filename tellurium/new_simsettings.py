# new simulation settings for tellurium
import tellurium as te

def simsettings(model):
    model.id_A = 2.0
    model.id_V = 3.0
    print("finished changing parameters")
    print(dict(model))
    return(model)
