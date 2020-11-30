
# Defintion for looping through a provided sequence, and counts the number of each basepair.
# takes provided sequence and passes it to the for loop inside
def countNucFrequency(seq):
    #Sets key values in tmpFreqDict and sets the value as zero
    tmpFreqDict = {"A": 0, "C": 0 , "G":0, "T":0}
    #For loop iterates through seq, for every key value found it adds 1 to the value for that key in the dictionary.
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
#Definition that takes provide sequence and replaces "T" with "U", returns RNA from DNA sequence.
def transcription(seq):
    return seq.replace("T","U")
#Definition that takes provide sequence and replaces "U" with "T", returns DNA from RNA sequence.
def revtranscription(seq):
    return seq.replace("U","T")
#Definition that takes in provide rna sequence and returns protein sequence.
def returnProtein(rna):
# Declare lists rnaCodons 
    rnaCodons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
 #Declare codons list 
    codons = []
    for i in range(0,len(rna),3):
        codons.append(rna[i:i+3])
    protein = ''.join([rnaCodons[codon] for codon in codons])
    return protein

