from .maingeneratesequencedefs import countNucFrequency

import random
import numpy as np
Nucleotiedes = ["A","C","T","G"]
#gc =int(input("Please enter desired gc%: ")) 

#x = int(input("Enter number of nucleotides to generate"))


def randnucleotidegen(x):
    
    numb_nuc = x
    
    compcountA =0 
    compcountC =0
    compcountT =0
    compcountG =0
     
    completerandDNAstr = ''.join([random.choice(Nucleotiedes) for nuc in range(numb_nuc)]) 


    for i in completerandDNAstr:
        if i =='A':
            compcountA = compcountA + 1
    for i in completerandDNAstr:
        if i =='C':
            compcountC = compcountC + 1    
    for i in completerandDNAstr:
        if i =='T':
            compcountT = compcountT + 1    
    for i in completerandDNAstr:
        if i =='G':
            compcountG = compcountG + 1   

    countgc = ((compcountC+compcountG)/numb_nuc)*100
    return completerandDNAstr, countgc