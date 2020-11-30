# import numpy as np for random sequence generation.
import numpy as np 
# import random for random sequence generation
import random 
# import counter from collections to obtain sequence content 
from collections import Counter    
# Declare lists 
AminoAcids = ["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
Hydro_Phobic =["G","A","V","L","I","F","Y","W","P","M"]
Hydro_Phillic =["C","S","T","N","Q"]
Acidic_Amino = ["D","E"]
Basic_Amino = ["R","K","H"]
# Definition that takes number of each amino acid type from user, sets the variables, and provides a random amino acid sequence. 
def randAminoAcidbynumb(a,b,c,x,y):
# Declare variables
    numbrandAA = a
    numbHpoAA = b
    numbHphAA = c
    numbAcidAA = x
    numbBaseAA = y
# series of np.random for loops for each respective amino acid type.
# each res variable uses counter from collections to recored number of each type of amino acid.
    
    randrandAAstr = ''.join([np.random.choice(AminoAcids)for amin in range(numbrandAA)])
    resa = Counter(randrandAAstr)
    
    randHpoAAstr = ''.join([np.random.choice(Hydro_Phobic) for amin in range (numbHpoAA)])
    resb = Counter(randHpoAAstr)
   

    randHphAAstr = ''.join([np.random.choice(Hydro_Phillic) for amin in range (numbHphAA)])
    resc = Counter(randHphAAstr)
    
   
    randAcidAAstr = ''.join([np.random.choice(Acidic_Amino) for amin in range (numbAcidAA)])
    resx = Counter(randAcidAAstr)
  
 
    randBaseAAstr = ''.join([np.random.choice(Basic_Amino) for amin in range (numbBaseAA)])
    resy = Counter(randBaseAAstr)
    # returns appended amino acid sequence from each amino acid type. Currently in the order below.        
    MixandMatchRandString = randrandAAstr + randHpoAAstr + randHphAAstr + randAcidAAstr + randBaseAAstr
    # returns generated amino acid sequence and counted amino acids in each sequence.
    return MixandMatchRandString, resa,resb,resc,resx,resy
    
    
# Definition that generates a x length random amino acid. 
def randAminoAcid(x):
    numbAA = x
    randAAstr = ''.join([np.random.choice(AminoAcids)for amin in range(numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res

# Definition that generates a x length random hydrophobic amino acid.   
def randHydrophobicAminoAcid(x1):
    numbAA = x1
    randAAstr = ''.join([np.random.choice(Hydro_Phobic) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res

    
#Definiton that generates a x length random hydrophillica amino acid.
def randHydroPhillicAminoAcid(x2):
    numbAA = x2
    randAAstr = ''.join([np.random.choice(Hydro_Phillic) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res
#Definition that generates a x length random acidic amino acid.
def randAcidicAmino(x3):

    numbAA = x3

    randAAstr = ''.join([np.random.choice(Acidic_Amino) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr,res
#Definition that generates a x length random basic amino acid.
def randBasicAmino(x4):
    numbAA = x4 
    
    randAAstr = ''.join([np.random.choice(Basic_Amino) for amin in range (numbAA)])
    res = Counter(randAAstr)

    return randAAstr,res

