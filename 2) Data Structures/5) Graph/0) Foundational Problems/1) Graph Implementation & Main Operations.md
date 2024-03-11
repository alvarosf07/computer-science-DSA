
# 1. Graph Implementation & Main Operations - Python

### Graph Implementation
```python
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        if src in self.adj_list and dest in self.adj_list:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)

    def remove_edge(self, src, dest):
        if src in self.adj_list and dest in self.adj_list:
            self.adj_list[src].remove(dest)
            self.adj_list[dest].remove(src)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                if vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)

    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
```
### Graph Operation I - Element Access
Accessing elements in a graph is done by accessing the adjacency list of a vertex:
```python
def get_neighbors(self, vertex):
    if vertex in self.adj_list:
        return self.adj_list[vertex]
    return []

```

### Graph Operation II - Element Modification
Modifying elements in a graph involves adding or removing edges between vertices:
```python
def add_edge(self, src, dest):
    if src in self.adj_list and dest in self.adj_list:
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

def remove_edge(self, src, dest):
    if src in self.adj_list and dest in self.adj_list:
        self.adj_list[src].remove(dest)
        self.adj_list[dest].remove(src)
```

### Graph Operation III - Element Insertion
Inserting elements into a graph involves adding new vertices and edges:
```python
def add_vertex(self, vertex):
    if vertex not in self.adj_list:
        self.adj_list[vertex] = []

def add_edge(self, src, dest):
    if src in self.adj_list and dest in self.adj_list:
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)
```

### Graph Operation IV - Element Deletion
Deleting elements from a graph involves removing vertices and edges:
```python
def remove_vertex(self, vertex):
    if vertex in self.adj_list:
        del self.adj_list[vertex]
        for v in self.adj_list:
            if vertex in self.adj_list[v]:
                self.adj_list[v].remove(vertex)

def remove_edge(self, src, dest):
    if src in self.adj_list and dest in self.adj_list:
        self.adj_list[src].remove(dest)
        self.adj_list[dest].remove(src)
```

<br/>
<br/>

# 2. Graph Implementation & Main Operations - C++
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <stdexcept>

using namespace std;

// Graph class manages the operations related to the graph
class Graph {
private:
    unordered_map<int, unordered_set<int>> adjList; // Adjacency list to represent the graph

public:
    // Function to add a vertex to the graph
    void addVertex(int vertex) {
        if (adjList.find(vertex) == adjList.end()) {
            adjList[vertex] = unordered_set<int>();
        }
    }

    // Function to add an edge between two vertices in the graph
    void addEdge(int from, int to) {
        addVertex(from);
        addVertex(to);
        adjList[from].insert(to);
    }

    // Function to remove an edge between two vertices in the graph
    void removeEdge(int from, int to) {
        if (adjList.find(from) != adjList.end()) {
            adjList[from].erase(to);
        }
    }

    // Function to check if an edge exists between two vertices in the graph
    bool hasEdge(int from, int to) const {
        if (adjList.find(from) != adjList.end()) {
            return adjList.at(from).find(to) != adjList.at(from).end();
        }
        return false;
    }

    // Function to remove a vertex and its incident edges from the graph
    void removeVertex(int vertex) {
        if (adjList.find(vertex) != adjList.end()) {
            for (auto& [from, neighbors] : adjList) {
                neighbors.erase(vertex);
            }
            adjList.erase(vertex);
        }
    }

    // Function to get the neighbors of a vertex in the graph
    const unordered_set<int>& getNeighbors(int vertex) const {
        if (adjList.find(vertex) != adjList.end()) {
            return adjList.at(vertex);
        }
        throw out_of_range("Vertex not found");
    }
};

```

<br/>
<br/>

# 3. Graph Implementation & Main Operations - JAVA
```java
import java.util.*;

// Graph class manages the operations related to the graph
class Graph {
    private Map<Integer, Set<Integer>> adjList; // Adjacency list to represent the graph

    // Constructor to initialize an empty graph
    Graph() {
        adjList = new HashMap<>();
    }

    // Function to add a vertex to the graph
    void addVertex(int vertex) {
        adjList.putIfAbsent(vertex, new HashSet<>());
    }

    // Function to add an edge between two vertices in the graph
    void addEdge(int from, int to) {
        addVertex(from);
        addVertex(to);
        adjList.get(from).add(to);
    }

    // Function to remove an edge between two vertices in the graph
    void removeEdge(int from, int to) {
        if (adjList.containsKey(from)) {
            adjList.get(from).remove(to);
        }
    }

    // Function to check if an edge exists between two vertices in the graph
    boolean hasEdge(int from, int to) {
        return adjList.containsKey(from) && adjList.get(from).contains(to);
    }

    // Function to remove a vertex and its incident edges from the graph
    void removeVertex(int vertex) {
        adjList.values().forEach(neighbors -> neighbors.remove(vertex));
        adjList.remove(vertex);
    }

    // Function to get the neighbors of a vertex in the graph
    Set<Integer> getNeighbors(int vertex) {
        if (!adjList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex not found");
        }
        return adjList.get(vertex);
    }
}

```

