#import countNucFrequency 
from .maingeneratesequencedefs import countNucFrequency
# import random and numpy functions 
import random
import numpy as np
# Declare Nucleotides list.
Nucleotiedes = ["A","C","T","G"]
#gc =int(input("Please enter desired gc%: ")) 

#x = int(input("Enter number of nucleotides to generate"))

# Definition that takes in variable x, and generates a random x length nucleotide sequence  
def randnucleotidegen(x):
    # Declare variables 
    numb_nuc = x
    
    compcountA =0 
    compcountC =0
    compcountT =0
    compcountG =0
    # Generates random DNA nucleotide sequence using random function.  
    completerandDNAstr = ''.join([random.choice(Nucleotiedes) for nuc in range(numb_nuc)]) 

# Foor loops to count each nucletide in the generated sequence above. 
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
# calculates the percent of gc by taking the sums of compcountc and compcountg divides by total number of nucleotides, numb_nuc and multiplies by 100.
    countgc = ((compcountC+compcountG)/numb_nuc)*100
    # returns nueclotide sequnce and gc percent 
    return completerandDNAstr, countgc