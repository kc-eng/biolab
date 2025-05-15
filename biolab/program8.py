PROGRAM_TEXT = '''import subprocess
from Bio import AlignIO

subprocess.run(["muscle", "-in", "eg.fasta", "-out", "aligned.fasta"])
alignment = AlignIO.read("aligned.fasta", "fasta")

print(alignment)'''

def __str__():
    return PROGRAM_TEXT

# The actual program code
import subprocess
from Bio import AlignIO

subprocess.run(["muscle", "-in", "eg.fasta", "-out", "aligned.fasta"])
alignment = AlignIO.read("aligned.fasta", "fasta")

print(alignment) 