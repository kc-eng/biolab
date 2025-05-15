import subprocess
from Bio import AlignIO
from io import StringIO
import os
import tempfile

def muscle_alignment(fasta_content):
    """Perform multiple sequence alignment using MUSCLE"""
    # Create temporary files
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.fasta') as temp_in:
        temp_in.write(fasta_content)
        input_file = temp_in.name
    
    output_file = input_file + '.aligned'
    
    try:
        # Run MUSCLE
        subprocess.run(["muscle", "-in", input_file, "-out", output_file], 
                     check=True, capture_output=True)
        
        # Read the alignment
        with open(output_file) as f:
            alignment = AlignIO.read(f, "fasta")
        
        # Clean up temporary files
        os.unlink(input_file)
        os.unlink(output_file)
        
        # Convert alignment to string representation
        output = StringIO()
        AlignIO.write(alignment, output, "fasta")
        return output.getvalue()
        
    except subprocess.CalledProcessError as e:
        return f"Error running MUSCLE: {e.stderr.decode()}"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Ensure cleanup
        if os.path.exists(input_file):
            os.unlink(input_file)
        if os.path.exists(output_file):
            os.unlink(output_file)

def __str__():
    """Return example output when the module is printed"""
    example_fasta = """>seq1
AGTACACTGGT
>seq2
AGTACGCTGGT
>seq3
AGTAGACTGGT"""
    return muscle_alignment(example_fasta) 