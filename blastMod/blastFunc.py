from  Bio.Blast import NCBIWWW
from  Bio.Blast import NCBIXML


# Function: runBlast - Takes search type and generated sequence and performs a BLAST search to look for similar sequences
def runBlast(runtype, sequence):
    #Format sequence using FASTA standard
    fastaFormat = ">Test\n%s\n" % sequence
    blastType = ""
    # Set correct type of BLAST search to be performed
    if(runtype == "n"):
        # Nucleotide
        blastType = "blastn"
        db = "nt"
    elif(runtype == "p"):
        # Amino Acid / Protein
        blastType = "blastp"
        db = "nr"
    else:
        # Raises Error if improper Blast type is set. This is for debugging purposes as the blast type cannot be implicitly changed by the user
        raise Exception("INVALID BLAST TYPE")
    # Run BLAST query
    result_handle = NCBIWWW.qblast(blastType, db, fastaFormat)
    # Read BLAST result into BLAST object
    blast_record = NCBIXML.read(result_handle)
    hitString = ""
    # Format result for display to User
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            hitString += ("*****Alignment*****\n sequence: %s\n length: %s\n e value: %s\n %s...\n %s...\n %s... " % (alignment.title, alignment.length, hsp.expect, hsp.query[0:75], hsp.match[0:75], hsp.sbjct[0:75]))

    # Return formatted result
    return hitString