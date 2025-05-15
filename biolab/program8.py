import subprocess
from Bio import AlignIO

def muscle_alignment(input_file="eg.fasta", output_file="aligned.fasta"):
    """Perform multiple sequence alignment using MUSCLE"""
    subprocess.run(["muscle", "-in", input_file, "-out", output_file])
    alignment = AlignIO.read(output_file, "fasta")
    return alignment

def __str__():
    """Return example output when the module is printed"""
    try:
        alignment = muscle_alignment()
        return str(alignment)
    except Exception as e:
        return f"Error: {str(e)}"

subprocess.run(["muscle", "-in", "eg.fasta", "-out", "aligned.fasta"])
alignment = AlignIO.read("aligned.fasta", "fasta")

print(alignment) 