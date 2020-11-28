import numpy as np 
import random 
from collections import Counter    
AminoAcids = ["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
Hydro_Phobic =["G","A","V","L","I","F","Y","W","P","M"]
Hydro_Phillic =["C","S","T","N","Q"]
Acidic_Amino = ["D","E"]
Basic_Amino = ["R","K","H"]

def randAminoAcidbynumb(a,b,c,x,y):

    numbrandAA = a
    numbHpoAA = b
    numbHphAA = c
    numbAcidAA = x
    numbBaseAA = y

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
           
    MixandMatchRandString = randrandAAstr + randHpoAAstr + randHphAAstr + randAcidAAstr + randBaseAAstr
    return MixandMatchRandString, resa,resb,resc,resx,resy
    
    

def randAminoAcid(x):
    numbAA = x
    randAAstr = ''.join([np.random.choice(AminoAcids)for amin in range(numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res

    
def randHydrophobicAminoAcid(x1):
    numbAA = x1
    randAAstr = ''.join([np.random.choice(Hydro_Phobic) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res

    

def randHydroPhillicAminoAcid(x2):
    numbAA = x2
    randAAstr = ''.join([np.random.choice(Hydro_Phillic) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr, res

def randAcidicAmino(x3):

    numbAA = x3

    randAAstr = ''.join([np.random.choice(Acidic_Amino) for amin in range (numbAA)])
    res = Counter(randAAstr)
    return randAAstr,res

def randBasicAmino(x4):
    numbAA = x4 
    
    randAAstr = ''.join([np.random.choice(Basic_Amino) for amin in range (numbAA)])
    res = Counter(randAAstr)

    return randAAstr,res

