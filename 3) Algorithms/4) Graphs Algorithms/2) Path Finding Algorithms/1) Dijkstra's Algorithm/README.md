# Dijkstra's Algorithm

> Dijkstra's algorithm is a popular algorithm used to find the shortest path between nodes in a graph with non-negative edge weights. It efficiently determines the shortest path from a single source node to all other nodes in the graph, producing a shortest path tree.

<br/>

## How Does Dijkstra's Algorithm Work?

Dijkstra's algorithm works by maintaining a set of tentative distances from the source node to each node in the graph. It iteratively selects the node with the smallest tentative distance, updates the distances to its neighbors, and marks the node as visited. This process continues until all nodes have been visited or the target node is reached.

<br/>

## Key Features of Dijkstra's Algorithm:

1. **Optimality:** Dijkstra's algorithm guarantees finding the shortest path from the source node to all other nodes in the graph with non-negative edge weights.

2. **Efficiency:** The algorithm has a time complexity of O(V^2) or O(ElogV) using a priority queue, where V is the number of vertices and E is the number of edges in the graph.

3. **Versatility:** Dijkstra's algorithm can be applied to various types of graphs, including directed and undirected graphs, weighted and unweighted graphs, and graphs with positive edge weights.

<br/>

## When to Use Dijkstra's Algorithm:

Dijkstra's algorithm is most commonly used in scenarios where:

- The goal is to find the shortest path between two nodes in a graph with non-negative edge weights.
- The graph is represented as a weighted graph with positive edge weights.
- The analysis requires determining the shortest path from a single source node to all other nodes in the graph.

<br/>

## Example of Dijkstra's Algorithm:

Consider the problem of finding the shortest path from node A to all other nodes in the graph:

```python
import heapq

def dijkstra(graph, source):
    # Initialize distances with infinity for all nodes except the source
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    # Priority queue to store nodes with their tentative distances
    pq = [(0, source)]
    
    while pq:
        # Pop node with the smallest tentative distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # Ignore outdated entries in the priority queue
        if current_distance > distances[current_node]:
            continue
            
        # Update distances to neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path is found, update the distance and push it into the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 6},
    'D': {}
}

# Run Dijkstra's algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest paths from node A:", shortest_paths)
```
