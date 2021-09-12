# file intended to include functions that may help with bad matlab exports
# Not further used as for the cases that were encountered, manual cleaning was performed
# Author: M. Stuke, 05-Sept-2019

# use libsbml: $ pip install python-libsbml

import libsbml 
from sbmlutils.io import read_sbml
from sbmlutils.validation import validate_doc
import re


def clean_string(string,
        TO_ASCII: bool = True,
        NO_SPACES: bool = True):
    #replaces non-ascii and empty spaces
    if TO_ASCII:
        string = re.sub(r'[^\x00-\x7F]+', '_', string) #r'[^\x00-\x7F]+' stands for non-ascii
    if NO_SPACES:
        string = re.sub(' ', '_', string)

    return(ascii(string))


def save_model(libsbml_model, path):
    #save libsbml Model object to ".sbml" path
    if (path[-5:] == ".sbml"):
        print("this is a .sbml path")
        libsbml_model.writeSBML(path)
        print("model has been saved to: \n", path)
    else:
        print("please give a valid filepath that ends with '.sbml'")

def errorcheck(filepath):
    # print error report from sbmlutils
    # returns True if without error
    doc = read_sbml(filepath); # import model to sbmlutils
    p = validate_doc(doc, units_consistency=False); # validate model
    return(p.is_valid())


def switch_reaction_IDforName(filepath, 
        CLEAN_NAMES: bool = True):
    # method to fix duplicate 'id' attribute values
    # By switching ID and names in reaction attributes
    reader = libsbml.SBMLReader()
    doc = reader.readSBML(filepath) #create libsbml.SBMLDocument object
    model = doc.getModel()
    print("switching names for ids:")
    print("first reaction before and after:")
    r1 = model.getReaction(0)
    print(r1)
    for i in range(model.getNumReactions()):
        reaction = model.getReaction(i)
        rname = reaction.getName()
        rid = reaction.getId()
        cl_name = clean_string(rname)
        print("clean name:", cl_name)
        libsbml.Reaction.setId(rid, cl_name)
    #test if worked:
    r1 = model.getReaction(0)
    print(r1)
    return(model)
