from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

def create_annotated_record(sequence=None, id="seq1", name="Example_gene", description="Example sequence"):
    """Create an annotated sequence record"""
    if sequence is None:
        sequence = "ATGCGTACGTAGCTAGCTAG"
    
    record = SeqRecord(
        Seq(sequence),
        id=id,
        name=name,
        description=description
    )
    
    record.annotations["gene"] = "ExampleGene"
    record.annotations["organism"] = "New species"
    record.annotations["function"] = "Hypothetical protein"
    record.features.append(
        SeqFeature(
            FeatureLocation(0, len(sequence)),
            type="gene"
        )
    )
    
    return {
        "name": record.name,
        "id": record.id,
        "description": record.description,
        "annotations": dict(record.annotations),
        "features": [str(f) for f in record.features]
    }

def __str__():
    """Return example output when the module is printed"""
    result = create_annotated_record()
    output = []
    for key, value in result.items():
        output.append(f"{key}: {value}")
    return "\n".join(output) 