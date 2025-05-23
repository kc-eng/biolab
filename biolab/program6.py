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

PROGRAM_TEXT = '''from Bio import Entrez, SeqIO

Entrez.email = "nikhilsingh.is22@bmsce.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")
print(record)
print(record.id)
print(record.description)
# print(record.features)
print(record.seq[:30])'''

def __str__():
    return PROGRAM_TEXT

def fetch_genbank_record(accession="NM_001301717", email="nikhilsingh.is22@bmsce.ac.in"):
    Entrez.email = email
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    print(record)
    print(record.id)
    print(record.description)
    # print(record.features)
    print(record.seq[:30])
    return record

# Execute the code directly when the module is run
Entrez.email = "nikhilsingh.is22@bmsce.ac.in"
handle = Entrez.efetch(db="nucleotide", id="NM_001301717", rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")
print(record)
print(record.id)
print(record.description)
# print(record.features)
print(record.seq[:30]) 