
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

```

<br/>
<br/>

# 3. Graph Implementation & Main Operations - JAVA
```java

```

