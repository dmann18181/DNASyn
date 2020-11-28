from  Bio.Blast import NCBIWWW
from  Bio.Blast import NCBIXML



def runBlast(runtype, sequence):
    # record = SeqRecord(Seq(sequence), id="testSeq", description="A test sequence")
    # s = Seq(sequence)
    fastaFormat = ">Test\n%s\n" % sequence
    blastType = ""
    # Set correct type of BLAST search to be performed
    if(runtype == "n"):
        blastType = "blastn"
        db = "nt"
    elif(runtype == "p"):
        blastType = "blastp"
        db = "nr"
    else:
        raise Exception("INVALID BLAST TYPE")
    # Run BLAST and return result
    result_handle = NCBIWWW.qblast(blastType, db, fastaFormat)
    blast_record = NCBIXML.read(result_handle)
    hitString = ""

    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            hitString += ("*****Alignment*****\n sequence: %s\n length: %s\n e value: %s\n %s...\n %s...\n %s... " % (alignment.title, alignment.length, hsp.expect, hsp.query[0:75], hsp.match[0:75], hsp.sbjct[0:75]))

    
    return hitString