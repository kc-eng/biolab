from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def create_genbank_record(sequence="AGTCTACGTACCCTAGGCCAAA", output_file="example.gb"):
    dna_seq = Seq(sequence)
    record = SeqRecord(
        dna_seq,
        id="seq1",
        name="Example_gene",
        description="Example gene sequence",
        annotations={
            "molecule_type": "DNA",  # Required for GenBank format
            "gene": "Example gene",
            "function": "hypothetical protein"
        }
    )
    
    # Open file for writing (without 'with')
    ofile = open(output_file, "w")
    SeqIO.write(record, ofile, "genbank")
    ofile.close()  # Must manually close the file
    
    # Open file for reading (without 'with')
    ifile = open(output_file, "r")
    record_read = SeqIO.read(ifile, "genbank")
    ifile.close()  # Must manually close the file
    
    print("Written successfully")
    print(record_read)
    return record_read

# Execute the code directly when the module is run
dna_seq = Seq("AGTCTACGTACCCTAGGCCAAA")

record = SeqRecord(
    dna_seq,
    id="seq1",
    name="Example_gene",
    description="Example gene sequence",
    annotations={
        "molecule_type": "DNA",  # Required for GenBank format
        "gene": "Example gene",
        "function": "hypothetical protein"
    }
)

# Define output file path
output_file = "example.gb"

# Open file for writing (without 'with')
ofile = open(output_file, "w")
SeqIO.write(record, ofile, "genbank")
ofile.close()  # Must manually close the file

print("Written successfully")

# Open file for reading (without 'with')
ifile = open(output_file, "r")
record_read = SeqIO.read(ifile, "genbank")
ifile.close()  # Must manually close the file

print(record_read)

PROGRAM_TEXT = '''from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dna_seq = Seq("AGTCTACGTACCCTAGGCCAAA")

record = SeqRecord(
    dna_seq,
    id="seq1",
    name="Example_gene",
    description="Example gene sequence",
    annotations={
        "molecule_type": "DNA",  # Required for GenBank format
        "gene": "Example gene",
        "function": "hypothetical protein"
    }
)

# Define output file path
output_file = "example.gb"

# Open file for writing (without 'with')
ofile = open(output_file, "w")
SeqIO.write(record, ofile, "genbank")
ofile.close()  # Must manually close the file

print("Written successfully")

# Open file for reading (without 'with')
ifile = open(output_file, "r")
record_read = SeqIO.read(ifile, "genbank")
ifile.close()  # Must manually close the file

print(record_read)'''

def __str__():
    return PROGRAM_TEXT

# The actual program code
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dna_seq = Seq("AGTCTACGTACCCTAGGCCAAA")

record = SeqRecord(
    dna_seq,
    id="seq1",
    name="Example_gene",
    description="Example gene sequence",
    annotations={
        "molecule_type": "DNA",  # Required for GenBank format
        "gene": "Example gene",
        "function": "hypothetical protein"
    }
)

# Define output file path
output_file = "example.gb"

# Open file for writing (without 'with')
ofile = open(output_file, "w")
SeqIO.write(record, ofile, "genbank")
ofile.close()  # Must manually close the file

print("Written successfully")

# Open file for reading (without 'with')
ifile = open(output_file, "r")
record_read = SeqIO.read(ifile, "genbank")
ifile.close()  # Must manually close the file

print(record_read) 