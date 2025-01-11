import random

def load_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by commas and strip any extra whitespace
            subj, pred, obj = map(str.strip, line.split(','))
            
            # Add the connection to the graph
            if subj not in graph:
                graph[subj] = []
            graph[subj].append((pred, obj))
            
    return graph

def bfs_subgraph(graph, start_node, target_triple_count):
    visited = set()
    used_nodes = set()  # Track all used nodes across all components
    subgraph_triples = []
    
    def bfs_component(start):
        """BFS within a single component."""
        queue = [start]
        local_triples = []
        while queue and len(local_triples) + len(subgraph_triples) < target_triple_count:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                used_nodes.add(node)
                # Get all the neighbors for the current node
                for pred, neighbor in graph.get(node, []):
                    # Add the triple (node, pred, neighbor) to the subgraph
                    local_triples.append((node, pred, neighbor))
                    if len(local_triples) + len(subgraph_triples) >= target_triple_count:
                        break
                    # If neighbor has not been visited already, add it to the queue
                    if neighbor not in visited:
                        queue.append(neighbor)
        return local_triples
    
    # Phase 1: Start BFS from the given start_node
    subgraph_triples.extend(bfs_component(start_node))
    
    # Phase 2: Explore other disconnected components if needed
    if len(subgraph_triples) < target_triple_count:
        for node in graph:
            if node not in used_nodes:
                subgraph_triples.extend(bfs_component(node))
            if len(subgraph_triples) >= target_triple_count:
                break

    return subgraph_triples

def write_subgraph(subgraph_triples, output_file):
    with open(output_file, 'w') as file:
        for subj, pred, obj in subgraph_triples:
            file.write(f"{subj},{pred},{obj}\n")

# Parameters
filename = 'data.txt'  # path to the RDF n-triple file
output_file = 'subgraph_output.txt'
start_node = '197114'  # Starting node for BFS (the very first node in the file)
fraction = 0.1  # Fraction of total triples desired in subgraph
print(f"Start node: {start_node}, subgraph size: {fraction*100}% of triples.")

# Step 1: Load the graph from the file
graph = load_graph(filename)
print("Graph loaded successfully!")

# Step 2: Calculate target triple count (10% of the total triples)
total_triples = sum(len(neighbors) for neighbors in graph.values())
target_triple_count = int(total_triples * fraction)
print(f"{fraction*100}% of triples is {target_triple_count}.")

# Step 3: Perform BFS to get the subgraph
subgraph_triples = bfs_subgraph(graph, start_node, target_triple_count)
print("Subgraph extracted successfully!")

# Step 4: Write the subgraph to an output file
write_subgraph(subgraph_triples, output_file)
print(f"Subgraph with approximately {fraction*100}% of triples saved to {output_file}")
