from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

def create_annotated_record(sequence="ATGCGTACGTAGCTAGCTAG"):
    record = SeqRecord(Seq(sequence), id="seq1", name="random ass name", description="some description")
    record.annotations["gene"] = "ExampleGene"
    record.annotations["organism"]="New species"
    record.annotations["function"]="Hypothetical protein"
    record.features.append(SeqFeature(FeatureLocation(0, 21), type="gene"))
    print(record.name)
    print(record.id)
    print(record.description)
    print(record.annotations)
    print(record.features)
    return record

# Execute the code directly when the module is run
record = SeqRecord(Seq("ATGCGTACGTAGCTAGCTAG"), id="seq1", name="random ass name", description="some description")
record.annotations["gene"] = "ExampleGene"
record.annotations["organism"]="New species"
record.annotations["function"]="Hypothetical protein"
record.features.append(SeqFeature(FeatureLocation(0, 21), type="gene"))
print(record.name)
print(record.id)
print(record.description)
print(record.annotations)
print(record.features)

PROGRAM_TEXT = '''from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

record = SeqRecord(Seq("ATGCGTACGTAGCTAGCTAG"), id="seq1", name="random ass name", description="some description")
record.annotations["gene"] = "ExampleGene"
record.annotations["organism"]="New species"
record.annotations["function"]="Hypothetical protein"
record.features.append(SeqFeature(FeatureLocation(0, 21), type="gene"))
print(record.name)
print(record.id)
print(record.description)
print(record.annotations)
print(record.features)'''

def __str__():
    return PROGRAM_TEXT

# The actual program code
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

record = SeqRecord(Seq("ATGCGTACGTAGCTAGCTAG"), id="seq1", name="random ass name", description="some description")
record.annotations["gene"] = "ExampleGene"
record.annotations["organism"]="New species"
record.annotations["function"]="Hypothetical protein"
record.features.append(SeqFeature(FeatureLocation(0, 21), type="gene"))
print(record.name)
print(record.id)
print(record.description)
print(record.annotations)
print(record.features) 