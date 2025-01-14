# Replace labels in triples with IDs based on entity and relation dictionaries

# File paths
triples_file = "data.txt"          
entities_file = "entity2id.txt"        
relations_file = "relation2id.txt"      
output_file = "data2.txt"  

# Load mappings
def load_mapping(file_path):
    mapping = {}
    with open(file_path, "r") as file:
        for line in file:
            label, id_ = line.strip().split(",")
            mapping[label] = id_.strip()
    return mapping

# Replace labels in triples with IDs
def convert_triples_to_ids(triples_file, entities, relations, output_file):
    with open(triples_file, "r") as input_file, open(output_file, "w") as output_file:
        for line in input_file:
            subject, relation, object_ = line.strip().split(",")
            subject_id = entities.get(subject.strip(), "UNKNOWN")
            relation_id = relations.get(relation.strip(), "UNKNOWN")
            object_id = entities.get(object_.strip(), "UNKNOWN")
            output_file.write(f"{subject_id},{relation_id},{object_id}\n")

def main():
    entity_mapping = load_mapping(entities_file)
    relation_mapping = load_mapping(relations_file)
    print("Mappings loaded")

    convert_triples_to_ids(triples_file, entity_mapping, relation_mapping, output_file)
    print(f"Triples with IDs written to {output_file}")

if __name__ == "__main__":
    main()
    
