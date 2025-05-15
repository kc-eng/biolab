from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from io import StringIO
import tempfile

def phylogenetic_tree(alignment_content, format="fasta"):
    """Construct a phylogenetic tree from aligned sequences"""
    # Parse the alignment from string
    alignment = AlignIO.read(StringIO(alignment_content), format)
    
    # Calculate distance matrix
    calculator = DistanceCalculator("identity")
    dm = calculator.get_distance(alignment)
    
    # Construct tree
    constructor = DistanceTreeConstructor()
    tree = constructor.build_tree(dm)
    
    # Convert tree to string representation
    output = StringIO()
    Phylo.write(tree, output, "newick")
    
    return {
        "newick": output.getvalue(),
        "ascii_tree": Phylo.draw_ascii(tree, file=StringIO()).getvalue()
    }

def __str__():
    """Return example output when the module is printed"""
    example_alignment = """>seq1
AGTACACTGGT
>seq2
AGTACGCTGGT
>seq3
AGTAGACTGGT"""
    
    try:
        result = phylogenetic_tree(example_alignment)
        return f"""Phylogenetic Tree Example:
Newick format:
{result['newick']}
ASCII representation:
{result['ascii_tree']}"""
    except Exception as e:
        return f"Error constructing tree: {str(e)}"

alignment = AlignIO.read("aligned.fasta", "fasta")
dm = DistanceCalculator("identity").get_distance(alignment)
tree = DistanceTreeConstructor().upgma(dm)

Phylo.draw(tree)
# Print ASCII tree
Phylo.draw_ascii(tree)

# Save to file
Phylo.write(tree, "tree.newick", "newick") 