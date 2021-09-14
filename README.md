[ODE.pptx](https://github.com/TDLemonNovecento/ODE_system/files/7028137/ODE.pptx)
# ODE_system
Small ODE system of an eye to play around
Additionally: Some python packages and uses thereof
to open .sbml files and run simulations

Packages considered: Tellurium, SBMLtoODE, libRoadRunner

change files in var.py according to desired file location before running
change booleans and method in main.py before running and import desired plotting regime
Plotting regimes need to be adapted to your specific model, this can be done in the respective plotfile.py

steps to get ackquainted:

open main.py, change all Booleans to False except for the first:
```python
$ # SET FLAGS FOR THIS RUN
$ CHECKFILE = True
$ FIXFILE = False #True
$ SAVE_NEWFILE = False
$ IMPORTFILE = False
$ SEE_SIMSETTINGS = False
$ CHANGE_SIMSETTINGS = False
$ RUN_SIMULATION = False #True
$ EXPORT_SIMRESULTS = False
$ GETODES = False
$ PLOT_EXAMPLE = False # Plotting requires import of specified plotting procedure
```

Create a python virtual environment running python 3 and containing tellurium as well as sbmlutils,
e.g. such as:
```python
$ # Conda env information:
$ conda create --name sbml_tellurium python=3
$ conda activate sbml_tellurium
$ pip install tellurium
$ pip install sbmlutils
```

Now run the main.py file inside this environment:
```python
$ python main.py #(using linux)
```
You should see black, red and blue text on your console:
ERROR:root:
--------------------------------------------------------------------------------
<SBMLDocument>
valid                    : FALSE
validation error(s)      : 8
validation warnings(s)   : 0
check time (s)           : 0.003
--------------------------------------------------------------------------------

The sbml file you just read contains errors. We want to fix them, for that, change the 
```python
  $ FIXFILE = True
```
Run the main.py file again. The file has been rewritten to the filename defined in var.py, In this case:
var.sbml_cleanfile is ./EYE/cleanfile.sbml
After the fix, the error message from sbmlutils reads:

--------------------------------------------------------------------------------
<SBMLDocument>
valid                    : TRUE
validation error(s)      : 0
validation warnings(s)   : 1
check time (s)           : 0.003
--------------------------------------------------------------------------------

You may want to fix manually the double id by searching for the variable name in the cleanfile.sbml and changing it.


Now, change the file to be imported into main.py to the fixed, clean file,
```python
$ ## SET FILEPATHS
$ #filepath = var.sbml_filename
$ new_filepath = var.sbml_cleanfile
$ filepath = new_filepath #for fixed files
```

and adapt the flags as follows:
```python
$ # SET FLAGS FOR THIS RUN
$ CHECKFILE = True
$ FIXFILE = False
$ IMPORTFILE = True
$ SEE_SIMSETTINGS = False
$ CHANGE_SIMSETTINGS = False
$ RUN_SIMULATION = False #True
$ EXPORT_SIMRESULTS = False
$ GETODES = False
$ PLOT_EXAMPLE = False
```

The lowest message in the console should read:
model of type <class 'tellurium.roadrunner.extended_roadrunner.ExtendedRoadRunner'> was successfully imported

Next, we can do some simulations and modeling:
and adapt the flags as follows:
```python
$ CHECKFILE = True
$ FIXFILE = False
$ IMPORTFILE = True
$ SEE_SIMSETTINGS = True
$ CHANGE_SIMSETTINGS = False
$ RUN_SIMULATION = True
$ EXPORT_SIMRESULTS = False
$ GETODES = False
$ PLOT_EXAMPLE = True
```

The console will show all settings of the model. As you can see, the Species initializations are 0.
  // Species initializations:
  id_A = 0;
  id_A has id_millimole_per_volume;
  id_V = 0;
  id_V has id_millimole_per_volume;
  id_R = 0;
  id_R has id_millimole_per_volume;
  id_S = 0;
  id_S has id_millimole_per_volume;
  id_P = 0;
  id_P has id_millimole_per_volume;


Let's change this.
go to ./tellurium/new_simsettings.py
Adapt changes as needed

Run again.

Issue: steps are not adequately changed, simulation runs with 50 steps only. 


