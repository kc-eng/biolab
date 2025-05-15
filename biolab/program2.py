from Bio import SeqIO
from io import StringIO

def read_fasta(file_name):
    """Read a FASTA file and return a list of records"""
    for record in SeqIO.parse(file_name,"fasta"):
        print("Header: ",record.description)
        print("Sequence: ",record.seq)
        print()

def __str__():
    """Return example output when the module is printed"""
    # Create an example FASTA string
    example_fasta = """>sequence1
ATGCGTACGT
>sequence2
GCTAGCTAGC"""
    
    # Create a StringIO object to simulate a file
    fasta_file = StringIO(example_fasta)
    
    # Parse the example
    records = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        records.append(f"Header: {record.description}\nSequence: {record.seq}\n")

fasta_file="eg.fasta"

read_fasta(fasta_file) 