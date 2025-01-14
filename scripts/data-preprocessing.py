import random
from sklearn.model_selection import train_test_split

# File paths
input_file = "data.txt"
train_file = "train.txt"
test_file = "test.txt"
val_file = "valid.txt"
entity_file = "entity2id.txt"
relation_file = "relation2id.txt"

def create_id_mappings(lines):
    """Creates ID mappings for entities and relations."""
    entity_set = set()
    relation_set = set()

    for line in lines:
        subject, relation, obj = line.strip().split(",")
        entity_set.add(subject)
        entity_set.add(obj)
        relation_set.add(relation)

    entity2id = {entity: idx for idx, entity in enumerate(sorted(entity_set))}
    relation2id = {relation: idx for idx, relation in enumerate(sorted(relation_set))}

    return entity2id, relation2id

def write_dict_to_file(file_path, dictionary):
    with open(file_path, "w") as file:
        for key, value in dictionary.items():
            file.write(f"{key},{value}\n")

def write_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.writelines(data)

def main():
    # Read the data
    with open(input_file, "r") as file:
        lines = file.readlines()
    print("Loaded the data")

    # Create entity and relation ID mappings
    entity2id, relation2id = create_id_mappings(lines)
    print("Created the entity and relation mappings")

    # Write mappings to files
    write_dict_to_file(entity_file, entity2id)
    write_dict_to_file(relation_file, relation2id)
    print("Wrote the mappings into files")

    # Split the data into train (90%) and temp (10%)
    train_data, temp_data = train_test_split(lines, test_size=0.1, random_state=42)

    # Split the temp data into test (5%) and validation (5%)
    test_data, val_data = train_test_split(temp_data, test_size=0.5, random_state=42)

    # Write the splits to their respective files
    write_to_file(train_file, train_data)
    write_to_file(test_file, test_data)
    write_to_file(val_file, val_data)
    print("Data successfully processed and split.")

if __name__ == "__main__":
    main()
