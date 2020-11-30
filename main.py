from tkinter.constants import CENTER
from Bio.Blast.Record import Alignment
from blastMod.blastFunc import *
from generator.AminoAcid import *
from generator.maingeneratesequencedefs import *
from generator.nucleotide import *
from generator.nucleotiderandom import *
from appJar import gui
import os
# Global variables
nucSeq = ""
aaSeq = ""
# Create GUI 
app = gui("DNASyn","1000x800")
app.setFont(size=12, family="Consolas")
# Function blastNucRunner - Calls RunBlast from blastFunc and returns result for Nucleotide
def blastNucRunner(seq):
    return runBlast("n", seq)
# Function blastAARunner - Calls RunBlast from blastFunc and returns result for Amino Acid
def blastAARunner(seq):
    return runBlast("p", seq)
# Function finishedBlast - Handles completion/Callback of threaded runBlast calls for Nucleotide
def finishedBlast(success):
    if success:
        message = success
    else:
        message = "Blast Failed"
    # Handles setting the Message: "BLAST Results" after Callback
    app.queueFunction(app.setMessage, "BLAST Results", message)
# Function finishedAABlast - Handles completion/Callback of threaded runBlast calls for Amino Acid
def finishedAABlast(success):
    if success:
        message = success
    else:
        message = "Blast Failed"
    # Handles setting the Message: "BLAST Results" after Callback
    app.queueFunction(app.setMessage, "aaRes", message)
# Function press - handles button press events for generation and exit buttons
def press(button):
    # Use global variables nucSeq and aaSeq
    global nucSeq
    global aaSeq
    # Exit application if Exit button is triggered
    if button == "Exit":
        app.stop()
    # Generates Nucleotide sequence and initiates threaded BLAST query call
    elif button == "Generate Nucleotide Sequence":
        # Get length of desired nucleotide sequence from input field
        nucCount = int(app.getEntry("Nucleotide Count"))
        # Call to generate random sequence
        randNuc = randnucleotidegen(nucCount)
        # Display generated sequence to User
        app.setMessage("Sequence", randNuc[0])
        app.setMessage("Sequence Percent GC", randNuc[1])
        # Set Global variable for use by save functionality
        nucSeq = randNuc[0]
        # Inform user BLAST query is being initiated
        app.setMessage("BLAST Results", "Running BLAST...\n Please Wait, this may take a few minutes")
        # Initiate threaded call to run BLAST query
        app.threadCallback(blastNucRunner, finishedBlast, randNuc[0])
    # Generates Amino Acid sequence and initiates threaded BLAST query call
    elif button == "Generate Amino Acid Sequence":
        # Get values from input fields
        hydrophob = int(app.getEntry("Number of Hydrophobic Amino Acids"))
        hydrophil = int(app.getEntry("Number of Hydrophilic Amino Acids"))
        acidic = int(app.getEntry("Number Acidic Amino Acids"))
        basic = int(app.getEntry("Number Basic Amino Acids"))
        aaCount = int(app.getEntry("Total Amino Acid Count"))
        # Call to generate random Amino Acid sequence
        randAA = randAminoAcidbynumb(aaCount, hydrophob, hydrophil, acidic, basic)
        # Display generated sequence to User
        app.setMessage("aaseq", randAA[0])
        # set global variable for later use by save functionality
        aaSeq = randAA[0]
        # Inform user BLAST query is being initiated
        app.setMessage("aaRes", "Running BLAST...\n Please Wait, this may take a few minutes")
        # Initiate threaded call to run BLAST query
        app.threadCallback(blastAARunner, finishedAABlast, randAA[0])
# Function saveFile - handles pressing of Save button for both Nucleotide and Amino Acid
def saveFile(button):
    # Handles trigger of Write Nucleotide to File button
    if button == "Write Nucleotide to File":
        # Opens file myNucSeq.txt for writing nucleotide sequence
        file = open("../myNucSeq.txt", 'w')
        # Write sequence to file 
        file.write(str(nucSeq))
        # Close File
        file.close()
        # Get path of written file
        path = os.path.realpath("../myNucSeq.txt")
        # Display location of file to user
        app.infoBox("Saved", "Nucleotide Sequence written to %s" % path)
    # Handles trigger of Write Amino Acid to File button
    elif button == "Write Amino Acid to File":
        # Opens myAASeq.txt for writing amino acid sequence
        file = open("../myAASeq.txt", 'w')
        # Write sequence to file
        file.write(aaSeq)
        # Close File
        file.close()
        # Get path of written file
        path = os.path.realpath("../myAASeq.txt")
        #Display location of file to user
        app.infoBox("Saved", "Amino Acid Sequence written to %s" % path)
# Creates tab for Nucleotide functionality
app.startTabbedFrame("Run Types")
app.startTab("Nucleotide")
app.addLabel("title1", "Nucleotide")
app.setLabelBg("title1", "blue")

# Input Fields
app.addLabel("Enter Desired Nucleotide Length:")
app.addNumericEntry("Nucleotide Count")
# Output Fields 
app.addLabel("Sequence Label", "Sequence:")
app.addMessage("Sequence", "Sequence Not Generated")
app.addLabel("Sequence GC Label", "Sequence Percent GC:")
app.addMessage("Sequence Percent GC", "Sequence Not Generated")
app.addLabel("Results Label", "BLAST Results:")
# Creates Scrollable area to preven overflow of result printout
app.startScrollPane("nucRes").config(width=800, height=200, border=2, borderwidth=2)
app.addMessage("BLAST Results", "BLAST Not Run")
app.stopScrollPane()
# Buttons for Nucleotide Tab
app.addButton("Generate Nucleotide Sequence", press)
app.addButton("Write Nucleotide to File", saveFile)
app.stopTab()

# Creates tab for Amino Acid Functionality
app.startTab("Amino Acid")
app.addLabel("title2", "Amino Acid")
app.setLabelBg("title2", "green")
#Input Fields
app.addLabelEntry("Total Amino Acid Count")
app.addLabelEntry("Number of Hydrophobic Amino Acids")
app.addLabelEntry("Number of Hydrophilic Amino Acids")
app.addLabelEntry("Number Acidic Amino Acids")
app.addLabelEntry("Number Basic Amino Acids")
# Output Fields
app.addLabel("aaSeqLabel", "Sequence:")
app.addMessage("aaseq", "Sequence Not Generated")
app.addLabel("aaResLabel", "BLAST Results:")
app.startScrollPane("aaRes").config(width=800, height=200, border=2, borderwidth=2)
app.addMessage("aaRes", "BLAST Not Run")
app.stopScrollPane()
# Buttons for Amino Acid Tab
app.addButton("Generate Amino Acid Sequence", press)
app.addButton("Write Amino Acid to File", saveFile)
app.stopTab()
app.stopTabbedFrame()
# Exit Button - Always visible
app.addButton("Exit", press)
# Run GUI app
app.go()

