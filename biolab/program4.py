from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO

def convert_fasta_to_genbank(fasta_content):
    """Convert FASTA format to GenBank format"""
    records = []
    
    # Parse FASTA content
    fasta_handle = StringIO(fasta_content)
    for record in SeqIO.parse(fasta_handle, "fasta"):
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
    
    # Write to GenBank format
    output = StringIO()
    SeqIO.write(records, output, "genbank")
    return output.getvalue()

def __str__():
    """Return example output when the module is printed"""
    example_fasta = """>seq1
ATGCGTACGT
>seq2
GCTAGCTAGC"""
    return convert_fasta_to_genbank(example_fasta)

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