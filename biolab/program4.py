from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO

def convert_fasta_to_genbank(input_file="eg.fasta", output_file="4th_genbank.gb"):
    records = []
    
    for record in SeqIO.parse(input_file, "fasta"):
        new = SeqRecord(
            record.seq,
            id=record.id,
            name="gene",
            description=record.description,
            annotations={
                "molecule_type": "DNA"
            }
        )
        records.append(new)
    
    file = open(output_file, "w")
    SeqIO.write(records, file, "genbank")
    file.close()

    file = open(output_file, "r")
    contents = list(SeqIO.parse(file, "genbank"))
    for content in contents:
        print(content)
    file.close()
    return contents

def __str__():
    """Return example output when the module is printed"""
    example_fasta = """>seq1
ATGCGTACGT
>seq2
GCTAGCTAGC"""
    return convert_fasta_to_genbank(example_fasta)

# Execute the code directly when the module is run
records = []

for record in SeqIO.parse("eg.fasta", "fasta"):
    new = SeqRecord(
        record.seq,
        id=record.id,
        name="gene",
        description=record.description,
        annotations={
            "molecule_type": "DNA"
        }
    )
    records.append(new)

file = open("4th_genbank.gb", "w")
SeqIO.write(records, file, "genbank")
file.close()

file = open("4th_genbank.gb", "r")
for content in SeqIO.parse(file, "genbank"):
    print(content)
file.close() 