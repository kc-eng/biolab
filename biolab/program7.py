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

def __str__():
    """Return example output when the module is printed"""
    result = pairwise_alignment()
    return f"""Pairwise Alignment Example:
Score: {result['score']}
Alignment:
{result['aligned']}""" 