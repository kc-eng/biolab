from Bio.PDB import *
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def visualize_structure(pdb_id="1A3N", save_plot=False):
    """Download and visualize a protein structure"""
    try:
        # Download PDB file
        pdbl = PDBList()
        cif_file = pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="mmCif")
        
        # Parse structure
        structure = MMCIFParser().get_structure(pdb_id, cif_file)
        
        # Get atom coordinates
        atoms = np.array([atom.coord for atom in structure.get_atoms()])
        
        # Create 3D plot
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(*atoms.T, s=5, alpha=0.5)
        ax.set_title(f"{pdb_id} Structure")
        
        if save_plot:
            # Save plot to bytes
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            img_str = base64.b64encode(buf.read()).decode()
            plt.close()
            return img_str
        else:
            plt.close()
            return {
                "pdb_id": pdb_id,
                "num_atoms": len(atoms),
                "dimensions": {
                    "x": (float(atoms[:,0].min()), float(atoms[:,0].max())),
                    "y": (float(atoms[:,1].min()), float(atoms[:,1].max())),
                    "z": (float(atoms[:,2].min()), float(atoms[:,2].max()))
                }
            }
            
    except Exception as e:
        return {"error": str(e)}

def __str__():
    """Return example output when the module is printed"""
    result = visualize_structure()
    if "error" in result:
        return f"Error: {result['error']}"
    else:
        return f"""Protein Structure Visualization Example:
PDB ID: {result['pdb_id']}
Number of atoms: {result['num_atoms']}
Dimensions:
  X: {result['dimensions']['x']}
  Y: {result['dimensions']['y']}
  Z: {result['dimensions']['z']}""" 