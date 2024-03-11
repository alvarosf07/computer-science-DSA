# Implementations with Graphs
Graphs are mainly used to implement some specific types of lists, matrices, and network representations:

### Structures implemented with Graphs:
  * **Adjacency List -** An adjacency list is a collection of lists or arrays, where each list/array represents the neighbors of a vertex in the graph. This data structure is used to represent sparse graphs and efficiently supports vertex and edge traversal, insertion, and deletion operations.
  * **Adjacency Matrix -** An adjacency matrix is a 2D array of size V x V, where V is the number of vertices in the graph. Each cell a[i][j] of the matrix represents an edge from vertex i to vertex j. This data structure is used to represent dense graphs and supports efficient edge lookup and modification in O(1) time complexity.
  * **Incidence Matrix -** An incidence matrix is a 2D array of size V x E, where V is the number of vertices and E is the number of edges in the graph. Each cell a[i][j] of the matrix represents the relationship between vertex i and edge j. This data structure is less commonly used due to its space inefficiency, but it supports efficient edge lookup and modification in O(1) time complexity.
  * **Edge List -** An edge list is a collection of tuples or objects representing the edges of the graph. Each tuple/object typically contains the source vertex, destination vertex, and optionally, the weight/cost of the edge. This data structure is used in algorithms such as Kruskal's algorithm for minimum spanning trees and Dijkstra's algorithm for shortest paths.

<br/>
