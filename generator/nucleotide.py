
from .maingeneratesequencedefs import countNucFrequency

import random
import numpy as np
Nucleotiedes = ["A","C","T","G"]
#gc =int(input("Please enter desired gc%: ")) 

#numb_nuc = int(input("Enter number of nucleotides to generate"))
#print("Enter probability of each bp, example for `'80%' gc input .4 for g and .4 for c .1 for A and .1 for T make sure your values sum up to 1")
#ProbA = float(input("Please enter probability for base A:" ))
#ProbC = float(input("Please enter probability for base C:" ))
#ProbT = float(input("Please enter probability for base T:" ))
#ProbG = float(input("Please enter probability for base G:" ))



def randnucleotidegenprob(a,c,t,g,x):

  
    ProbA = a
    ProbC = c
    ProbT = t
    ProbG = g
    numb_nuc = x 
    countA =0 
    countC =0
    countT =0
    countG =0
    
    P = (ProbA, ProbC,ProbT,ProbG)
    randDNAstr = ''.join([np.random.choice(Nucleotiedes, p=P)for nuc in range(numb_nuc)])

    for i in randDNAstr:
        if i =='A':
            countA = countA + 1

    for i in randDNAstr:
        if i =='C':
            countC = countC + 1    
    for i in randDNAstr:
        if i =='T':
            countT = countT + 1    
    for i in randDNAstr:
        if i =='G':
            countG = countG + 1    
    countgc = ((countC+countG)/numb_nuc)*100
    return randDNAstr,countgc 
   


