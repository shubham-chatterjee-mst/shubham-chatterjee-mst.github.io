import numpy as np

# Initialize the adjacency matrix
INF = float('inf')
graph = [
    [0, 5, 3, INF, INF],
    [5, 0, 2, INF, 6],
    [3, 2, 0, 4, INF],
    [INF, INF, 4, 0, 1],
    [INF, 6, INF, 1, 0]
]

def dijkstra(adj, source):
    num_nodes = len(adj)
    
    # Step 1: Initialize path[], status[], and pred[] arrays
    path = [INF] * num_nodes  # Distance from source to each node
    status = ["TEMP"] * num_nodes  # TEMP for all nodes initially
    pred = [None] * num_nodes  # Predecessors initialized to None
    
    # Step 4: Set distance from source to itself
    path[source] = 0
    
    while True:
        # Step 5-6: Find the node with the minimum temporary distance
        current = None  # Placeholder for current node
        min_distance = INF
        
        # TODO: Implement the logic to find the node with the minimum temporary distance
                
        # Step 7: Check if all reachable nodes are processed
        if current is None:
            break  # All reachable nodes processed
        
        # Step 10: Mark current node as permanent
        status[current] = "PERM"
        
        # Step 11-15: Update distances of each adjacent node
        for i in range(num_nodes):
            # TODO: Check if there's an edge between `current` and `i`, and `i` is TEMP
                       
            # TODO: If a shorter path is found, update `path[i]` and `pred[i]`
       
    
    return path, pred

# Example usage
source_node = 0  # Assuming 'A' is node 0
distances, predecessors = dijkstra(graph, source_node)

# Print results
print("Shortest distances from source node A:")
for i, dist in enumerate(distances):
    print(f"Distance to node {chr(i + ord('A'))}: {dist}")

print("\nPredecessor nodes for each node:")
for i, pred in enumerate(predecessors):
    if pred is not None:
        print(f"Predecessor of node {chr(i + ord('A'))}: {chr(pred + ord('A'))}")
    else:
        print(f"Predecessor of node {chr(i + ord('A'))}: None")
