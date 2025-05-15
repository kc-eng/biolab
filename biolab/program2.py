from Bio import SeqIO
from io import StringIO

PROGRAM_TEXT = '''from Bio import SeqIO

def read_fasta(file_name):
    for record in SeqIO.parse(file_name,"fasta"):
        print("Header: ",record.description)
        print("Sequence: ",record.seq)
        print()
   
fasta_file="eg.fasta"
read_fasta(fasta_file)'''

def __str__():
    return PROGRAM_TEXT

# The actual program code
from Bio import SeqIO

def read_fasta(file_name):
    """Read a FASTA file and return a list of records"""
    for record in SeqIO.parse(file_name,"fasta"):
        print("Header: ",record.description)
        print("Sequence: ",record.seq)
        print()
    return list(SeqIO.parse(file_name, "fasta"))

# Execute the code directly when the module is run
fasta_file="eg.fasta"
read_fasta(fasta_file) 