# Depth-First Search (DFS)

> Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It traverses a graph or tree depthwise rather than breadthwise, making it useful for certain tasks such as finding connected components, detecting cycles, and solving maze problems.

<br/>

## How Does Depth-First Search Work?

Depth-First Search works by starting at an initial node and exploring as far as possible along each branch before backtracking. It maintains a stack (or uses recursion) to keep track of the nodes to visit and the order in which they are visited. The algorithm continues this process until all reachable nodes have been visited.

<br/>

## Step-by-Step Guide of Depth-First Search:

1. **Start at Initial Node:** Begin the search at the initial node of the graph or tree.

2. **Explore Neighbors:** Visit a neighbor of the current node that has not been visited yet. If all neighbors have been visited or there are no neighbors, backtrack to the previous node.

3. **Repeat:** Continue exploring neighbors recursively until all reachable nodes have been visited or the search criteria are met.

4. **Backtracking:** When backtracking, return to the previous node and explore any unvisited neighbors from there.

For a visual demonstration of Depth-First Search, you can watch this [video](https://www.youtube.com/watch?v=TIbUeeksXcI) tutorial.

<br/>

## Key Features of Depth-First Search:

1. **Completeness:** Depth-First Search explores all reachable nodes in a graph or tree, ensuring that no node is left unvisited.

2. **Memory Efficiency:** Depth-First Search requires minimal memory overhead as it only needs to store the current path and backtrack when necessary.

3. **Versatility:** Depth-First Search can be applied to various types of graphs, including directed and undirected graphs, weighted and unweighted graphs, and graphs with cycles.

<br/>

## When to Use Depth-First Search:

Depth-First Search is most commonly used in scenarios where:

- The goal is to explore all reachable nodes in a graph or tree.
- The search criteria involve traversing as far as possible along each branch before backtracking.
- Backtracking is allowed or necessary to explore all possible paths.

<br/>

## Example of Depth-First Search:

Consider the problem of finding a path from node A to node G in the following graph:

```markdown
     A
   /   \
  B     C
 / \   / \
D   E F   G
```

Applying Depth-First Search, we would start at node A, explore as far as possible along each branch, and eventually find a path from A to G.



