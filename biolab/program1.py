from Bio.Seq import Seq

def dna_manipulation():
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
    
    return {
        "DNA Sequence": str(dna_seq),
        "Sliced Sequence": str(sliced_seq),
        "Concatenated": str(concatenated_seq),
        "RNA": str(rna_seq),
        "Protein": str(protein_seq)
    }

# Execute the code directly when the module is run
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