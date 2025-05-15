from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from io import StringIO

def create_genbank(sequence=None, id="seq1", name="Example_gene", description="Example gene sequence"):
    """Create a GenBank record from a sequence"""
    if sequence is None:
        sequence = "AGTCTACGTACCCTAGGCCAAA"
    
    dna_seq = Seq(sequence)
    record = SeqRecord(
        dna_seq,
        id=id,
        name=name,
        description=description,
        annotations={
            "molecule_type": "DNA",
            "gene": name,
            "function": "hypothetical protein"
        }
    )
    
    # Write to a string buffer
    output = StringIO()
    SeqIO.write(record, output, "genbank")
    return output.getvalue()

def __str__():
    """Return example output when the module is printed"""
    return create_genbank() 