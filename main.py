from tkinter.constants import CENTER
from Bio.Blast.Record import Alignment
from blastMod.blastFunc import *
from generator.AminoAcid import *
from generator.maingeneratesequencedefs import *
from generator.nucleotide import *
from generator.nucleotiderandom import *
from appJar import gui
import os

nucSeq = ""
aaSeq = ""

app = gui("DNASyn","1000x800")
app.setFont(size=12, family="Consolas")

def blastNucRunner(seq):
    return runBlast("n", seq)

def blastAARunner(seq):
    return runBlast("p", seq)

def finishedBlast(success):
    if success:
        message = success
    else:
        message = "Blast Failed"
    app.queueFunction(app.setMessage, "BLAST Results", message)

def finishedAABlast(success):
    if success:
        message = success
    else:
        message = "Blast Failed"
    app.queueFunction(app.setMessage, "aaRes", message)

def press(button):
    global nucSeq
    global aaSeq
    if button == "Exit":
        app.stop()
    elif button == "Generate Nucleotide Sequence":
        # gcPercent = float(app.getEntry("G/C Percent"))
        nucCount = int(app.getEntry("Nucleotide Count"))
        randNuc = randnucleotidegen(nucCount)
        app.setMessage("Sequence", randNuc[0])
        app.setMessage("Sequence Percent GC", randNuc[1])
        nucSeq = randNuc[0]
        app.setMessage("BLAST Results", "Running BLAST...\n Please Wait, this may take a few minutes")
        app.threadCallback(blastNucRunner, finishedBlast, randNuc[0])
    elif button == "Generate Amino Acid Sequence":
        hydrophob = int(app.getEntry("Number of Hydrophobic Amino Acids"))
        hydrophil = int(app.getEntry("Number of Hydrophilic Amino Acids"))
        acidic = int(app.getEntry("Number Acidic Amino Acids"))
        basic = int(app.getEntry("Number Basic Amino Acids"))
        aaCount = int(app.getEntry("Total Amino Acid Count"))
        randAA = randAminoAcidbynumb(aaCount, hydrophob, hydrophil, acidic, basic)
        app.setMessage("aaseq", randAA[0])
        aaSeq = randAA[0]
        app.setMessage("aaRes", "Running BLAST...\n Please Wait, this may take a few minutes")
        app.threadCallback(blastAARunner, finishedAABlast, randAA[0])

def saveFile(button):
    if button == "Write Nucleotide to File":
        file = open("../myNucSeq.txt", 'w') 
        file.write(str(nucSeq))
        file.close()
        path = os.path.realpath("../myNucSeq.txt")
        app.infoBox("Saved", "Nucleotide Sequence written to %s" % path)
            
    elif button == "Write Amino Acid to File":
        file = open("../myAASeq.txt", 'w')
        file.write(aaSeq)
        file.close()
        path = os.path.realpath("../myAASeq.txt")
        app.infoBox("Saved", "Nucleotide Sequence written to %s" % path)

app.startTabbedFrame("Run Types")
app.startTab("Nucleotide")
app.addLabel("title1", "Nucleotide")
app.setLabelBg("title1", "blue")

# app.addLabelEntry("G/C Percent")
app.addLabel("Enter Desired Nucleotide Length:")
app.addNumericEntry("Nucleotide Count")
app.addLabel("Sequence Label", "Sequence:")
app.addMessage("Sequence", "Sequence Not Generated")
app.addLabel("Sequence GC Label", "Sequence Percent GC:")
app.addMessage("Sequence Percent GC", "Sequence Not Generated")
app.addLabel("Results Label", "BLAST Results:")
app.startScrollPane("nucRes").config(width=800, height=200, border=2, borderwidth=2)
app.addMessage("BLAST Results", "BLAST Not Run")
app.stopScrollPane()
app.addButton("Generate Nucleotide Sequence", press)
app.addButton("Write Nucleotide to File", saveFile)
app.stopTab()


app.startTab("Amino Acid")
app.addLabel("title2", "Amino Acid")
app.setLabelBg("title2", "green")

app.addLabelEntry("Total Amino Acid Count")
app.addLabelEntry("Number of Hydrophobic Amino Acids")
app.addLabelEntry("Number of Hydrophilic Amino Acids")
app.addLabelEntry("Number Acidic Amino Acids")
app.addLabelEntry("Number Basic Amino Acids")

app.addLabel("aaSeqLabel", "Sequence:")

app.addMessage("aaseq", "Sequence Not Generated")
app.addLabel("aaResLabel", "BLAST Results:")
app.startScrollPane("aaRes").config(width=800, height=200, border=2, borderwidth=2)
app.addMessage("aaRes", "BLAST Not Run")
app.stopScrollPane()
app.addButton("Generate Amino Acid Sequence", press)
app.addButton("Write Amino Acid to File", saveFile)
app.stopTab()
app.stopTabbedFrame()

app.addButton("Exit", press)

app.go()

