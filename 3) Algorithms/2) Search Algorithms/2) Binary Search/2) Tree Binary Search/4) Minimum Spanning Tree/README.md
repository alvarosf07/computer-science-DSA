# Minimum Spanning Tree (MST)

> A Minimum Spanning Tree (MST) of a connected, undirected graph is a subset of the edges that forms a tree and includes all the vertices of the original graph. The MST has the minimum possible total edge weight among all trees that can be formed from the graph.

<br/>

## How Does Minimum Spanning Tree Work?

Minimum Spanning Tree algorithms aim to find the subset of edges that form the minimum spanning tree of a graph. These algorithms typically start with an empty set of edges and iteratively add edges that satisfy certain conditions until a spanning tree is formed.

<br/>

## Step-by-Step Guide of Minimum Spanning Tree:

1. **Start with an Empty Set of Edges:** Begin with an empty set of edges that will eventually form the Minimum Spanning Tree.

2. **Add Edges to the Set:** Iterate through the edges of the graph and add edges to the set one by one, ensuring that the resulting subset forms a spanning tree.

3. **Ensure Connectivity:** Ensure that the subset of edges maintains connectivity, i.e., there should be a path between every pair of vertices in the tree.

4. **Minimize Total Edge Weight:** Choose edges that minimize the total edge weight of the spanning tree, ensuring that the tree is a Minimum Spanning Tree.

For a visual demonstration of Minimum Spanning Tree algorithms, you can watch this [video](https://www.youtube.com/watch?v=TbKGXq8aE7k) tutorial.

<br/>

## Algorithms to Solve Minimum Spanning Tree:

1. **Kruskal's Algorithm:** A greedy algorithm that starts with the smallest edge and adds edges to the tree while avoiding cycles. It maintains a disjoint set data structure to ensure connectivity.

2. **Prim's Algorithm:** Another greedy algorithm that starts with an arbitrary vertex and grows the tree by adding the shortest edge that connects the tree to a new vertex until all vertices are included.

<br/>

## Key Features of Minimum Spanning Tree:

1. **Optimality:** Minimum Spanning Tree algorithms guarantee finding the subset of edges with the minimum possible total edge weight.

2. **Versatility:** Minimum Spanning Tree algorithms can be applied to various types of graphs, including weighted and unweighted graphs, and graphs with cycles.

3. **Efficiency:** Kruskal's and Prim's algorithms have efficient time complexities, making them suitable for finding Minimum Spanning Trees in large graphs.

<br/>

## When to Use Minimum Spanning Tree:

Minimum Spanning Tree algorithms are most commonly used in scenarios where:

- The goal is to find the subset of edges with the minimum total weight that connects all vertices of a graph.
- The graph represents a network with weighted connections, such as road networks, communication networks, or pipeline networks.

<br/>

## Example of Minimum Spanning Tree:

Consider the problem of finding the Minimum Spanning Tree of the following weighted graph:
```markdown
     A
    /|\
  5/ | \7
  /  |  \
 B---2---C
 6\  |  /
  4\ | /3
    \|/
     D
```

This graph represents a network of vertices (A, B, C, D) connected by edges with different weights. To find the Minimum Spanning Tree, we aim to select a subset of edges that connect all vertices with the minimum total weight.

We can apply Kruskal's or Prim's algorithm to find the Minimum Spanning Tree:

1. Kruskal's Algorithm:
   * Start with an empty set of edges.
   * Sort all the edges by weight in non-decreasing order.
   * Iterate through the sorted edges and add each edge to the set if it does not form a cycle with the edges already selected.
   * Continue until all vertices are connected, and no cycles are formed.

2. Prim's Algorithm:
   * Start with an arbitrary vertex (let's say vertex A) and mark it as visited.
   * Maintain a priority queue or heap to store edges sorted by weight.
   * While there are unvisited vertices:
     * Select the shortest edge that connects a visited vertex to an unvisited vertex.
     * Mark the unvisited vertex as visited and add the edge to the Minimum Spanning Tree.

Applying either algorithm to the given graph, we would start with an empty set of edges and iteratively add edges until all vertices are connected without forming cycles. The resulting set of edges forms the Minimum Spanning Tree of the graph.

For example, applying Kruskal's algorithm, we would select the edges with weights 2, 3, and 4 first, as they form the minimum weight connections between vertices. Then, we would add edges with weights 5 and 6 to complete the Minimum Spanning Tree.

In this way, the algorithm ensures that the Minimum Spanning Tree has the minimum total weight while connecting all vertices of the graph.


