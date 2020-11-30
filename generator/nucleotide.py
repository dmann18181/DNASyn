# Import countNucFrequency from maingeneratedsequencedefs
from .maingeneratesequencedefs import countNucFrequency
#import random
import random
#import numpy
import numpy as np
#Declare Nucleotides list
Nucleotiedes = ["A","C","T","G"]


#Definition that takes in probability variables and numb_nuc and generates a nucleotide sequence by probability.
def randnucleotidegenprob(a,c,t,g,x):

  #Set variables
    ProbA = a
    ProbC = c
    ProbT = t
    ProbG = g
    numb_nuc = x 
    countA =0 
    countC =0
    countT =0
    countG =0
    #set probabilities 
    P = (ProbA, ProbC,ProbT,ProbG)
    # random string generation using numpy and random 
    randDNAstr = ''.join([np.random.choice(Nucleotiedes, p=P)for nuc in range(numb_nuc)])
    # series of for loops iterating through randDNAstr to determine counts for each basepair. 
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
   


