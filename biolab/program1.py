from Bio.Seq import Seq

def dna_manipulation(dna_sequence=None):
    if dna_sequence is None:
        dna_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC"
    
    dna_seq = Seq(dna_sequence)
    result = {
        "DNA Sequence": str(dna_seq),
        "Sliced Sequence": str(dna_seq[3:11]),
        "Concatenated": str(dna_seq[3:11] + Seq("TGCA")),
        "RNA": str(dna_seq[3:11].transcribe()),
        "Protein": str(dna_seq[3:11].translate())
    }
    return result

def __str__():
    """Return the example output when the module is printed"""
    result = dna_manipulation()
    output = []
    for key, value in result.items():
        output.append(f"{key}: {value}")
    return "\n".join(output) 