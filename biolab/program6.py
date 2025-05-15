from Bio import Entrez, SeqIO
from io import StringIO

def fetch_genbank(accession="NM_001301717", email=None):
    """Fetch a GenBank record from NCBI"""
    if email is None:
        raise ValueError("An email address is required for accessing NCBI databases")
    
    Entrez.email = email
    try:
        handle = Entrez.efetch(
            db="nucleotide",
            id=accession,
            rettype="gb",
            retmode="text"
        )
        record = SeqIO.read(handle, "genbank")
        handle.close()
        
        return {
            "id": record.id,
            "description": record.description,
            "sequence_preview": str(record.seq[:30]),
            "length": len(record.seq)
        }
    except Exception as e:
        return {"error": str(e)}

def __str__():
    """Return example output when the module is printed"""
    return """To use this module, call:
fetch_genbank(accession="NM_001301717", email="your.email@example.com")

Example output format:
{
    "id": "NM_001301717",
    "description": "Homo sapiens ...",
    "sequence_preview": "ATGCGT...",
    "length": 1234
}"""

Entrez.email = "nikhilsingh.is22@bmsce.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")
print(record)
print(record.id)
print(record.description)
# print(record.features)
print(record.seq[:30]) 