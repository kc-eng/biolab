from Bio.Align import PairwiseAligner

def pairwise_alignment(seq1="AGTACACTGGT", seq2="AGTACGCTGGT"):
    """Perform pairwise sequence alignment"""
    aligner = PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    
    # Get the first alignment
    alignment = alignments[0]
    
    return {
        "score": alignment.score,
        "aligned": str(alignment),
        "sequences": {
            "sequence1": seq1,
            "sequence2": seq2
        }
    }

PROGRAM_TEXT = '''from Bio.Align import PairwiseAligner
aligner = PairwiseAligner()
alignment = aligner.align("AGTACACTGGT", "AGTACGCTGGT")
print(alignment)
print(alignment[0])
print(alignment[2])
print(alignment[0].score)'''

def __str__():
    return PROGRAM_TEXT

def perform_alignment(seq1="AGTACACTGGT", seq2="AGTACGCTGGT"):
    aligner = PairwiseAligner()
    alignment = aligner.align(seq1, seq2)
    print(alignment)
    print(alignment[0])
    print(alignment[2])
    print(alignment[0].score)

# Execute the code directly when the module is run
aligner = PairwiseAligner()
alignment = aligner.align("AGTACACTGGT", "AGTACGCTGGT")
print(alignment)
print(alignment[0])
print(alignment[2])
print(alignment[0].score) 