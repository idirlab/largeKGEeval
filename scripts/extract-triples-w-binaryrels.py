def filter_ids(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                try:
                    label, id_ = line.split(',')
                    label, id_ = label.strip(), id_.strip()
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    continue

                if '-' not in label:
                    outfile.write(f"{id_}\n")

        print(f"Filtered IDs have been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def filter_triples(triples_file, ids_file, output_file):
    try:
        # Read the binary relation IDs 
        with open(ids_file, 'r') as id_file:
            valid_ids = set(id_.strip() for id_ in id_file if id_.strip())

        # Filter triples based on binary/nary relations
        with open(triples_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                try:
                    subject, relation, obj = line.split(',')
                    subject, relation, obj = subject.strip(), relation.strip(), obj.strip()
                except ValueError:
                    print(f"Skipping invalid triple: {line}")
                    continue

                if relation in valid_ids:
                    outfile.write(f"{subject},{relation},{obj}\n")

        print(f"Filtered triples have been written to {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    dictionary_file = "relation2id.txt"  # relation dictionary file containing label, ID pairs
    filtered_ids_file = "binaryrelation_ids.txt"  # Output file for IDs without '-' in labels
    triples_file = "data.txt"  # data file containing subject, relation, object triples
    filtered_triples_file = "filtered_triples.txt"  # Output file for filtered triples (with only binary relations)

    #filter_ids(dictionary_file, filtered_ids_file)
    filter_triples(triples_file, filtered_ids_file, filtered_triples_file)

if __name__ == "__main__":
    main()
