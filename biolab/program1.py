from Bio.Seq import Seq

dna_seq=Seq("ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")
print("DNA Sequence: ", dna_seq)

sliced_seq=dna_seq[3:11]
print("Sliced Sequence: ", sliced_seq)

another_seq=Seq("TGCA")
concatenated_seq=sliced_seq+another_seq

print("Concatenated: ",concatenated_seq)

rna_seq=concatenated_seq.transcribe()
print("RNA: ",rna_seq)

protein_seq=rna_seq.translate()
print("Protein: ",protein_seq)

def __str__():
    """Return the example output when the module is printed"""
    result = dna_manipulation()
    output = []
    for key, value in result.items():
        output.append(f"{key}: {value}")
    return "\n".join(output) 