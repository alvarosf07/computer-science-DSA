# Breadth-First Search (BFS)

> Breadth-First Search (BFS) is a graph traversal algorithm that explores all neighbors of a node before moving on to the next level of nodes. It traverses a graph or tree level by level, starting from the root node, and is often used to find the shortest path between two nodes, detect connected components, and solve puzzles like the shortest path in a maze.

<br/>

## How Does Breadth-First Search Work?

Breadth-First Search works by exploring all neighbors of a node before moving on to the next level of nodes. It maintains a queue to keep track of the nodes to visit and the order in which they are visited. The algorithm continues this process until all reachable nodes have been visited.

<br/>

## Step-by-Step Guide of Breadth-First Search:

1. **Start at Initial Node:** Begin the search at the initial node of the graph or tree.

2. **Visit Neighbors:** Visit all neighbors of the current node. Add them to the queue if they have not been visited yet.

3. **Dequeue and Repeat:** Dequeue the next node from the queue and repeat step 2 for its neighbors.

4. **Continue Until Queue is Empty:** Repeat steps 2-3 until the queue is empty, indicating that all reachable nodes have been visited.

For a visual demonstration of Breadth-First Search, you can watch this [video](https://www.youtube.com/watch?v=s-CYnVz-uh4) tutorial.

<br/>

## Key Features of Breadth-First Search:

1. **Optimality:** Breadth-First Search guarantees finding the shortest path between two nodes in an unweighted graph.

2. **Completeness:** Breadth-First Search explores all reachable nodes in a graph or tree, ensuring that no node is left unvisited.

3. **Memory Efficiency:** Breadth-First Search requires minimal memory overhead as it only needs to store the current level of nodes being visited.

<br/>

## When to Use Breadth-First Search:

Breadth-First Search is most commonly used in scenarios where:

- The goal is to find the shortest path between two nodes in an unweighted graph.
- The search criteria involve traversing level by level in a graph or tree.
- Memory efficiency is important, and the graph or tree is relatively small.

<br/>

## Example of Breadth-First Search:

Consider the problem of finding the shortest path from node A to node G in the following graph:
```markdown
     A
   /   \
  B     C
 / \   / \
D   E F   G
```

Applying Breadth-First Search, we would start at node A, visit its neighbors B and C, then visit the neighbors of B and C, continuing level by level until we reach node G.


