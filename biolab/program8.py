import subprocess
from Bio import AlignIO

def run_muscle(input_file="eg.fasta", output_file="aligned.fasta"):
    subprocess.run(["muscle", "-in", input_file, "-out", output_file])
    alignment = AlignIO.read(output_file, "fasta")
    print(alignment)
    return alignment

# Execute the code directly when the module is run
subprocess.run(["muscle", "-in", "eg.fasta", "-out", "aligned.fasta"])
alignment = AlignIO.read("aligned.fasta", "fasta")
print(alignment) 