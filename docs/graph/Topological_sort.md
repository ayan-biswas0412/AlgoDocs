# Topological Sorting
You are given a directed graph with n vertices and m edges. You have to number the vertices so that every edge leads from the vertex with a smaller number assigned to the vertex with a larger one.
Topological Sorting is possible if and only if the graph is a Directed Acyclic Graph.
There may exist multiple different topological orderings for a given directed acyclic graph.

## Algorithm

```
Algorithm 
Step 1) Identify vertices that have no incoming edges. Select that vertex as starting vertex of a graph. 
Step 2) Delete the starting vertex or the vertex with no incoming edges and delete all its outgoing edges from the graph.
Step 3) Place the deleted vertex in the output list. 
Step 4) Repeat Steps 1-3 until the graph is empty.

```

## Pseudocode

```
visit(self,n,visited,T):

   mark n as visited
   for all vertices i which is adjacent with n, do
      if i is not visited, then
         visit(i, visited, T)
   push n into a stack


topological_sort(self):
   initially mark all nodes as unvisited
   for all nodes v of the graph, do
      if v is not visited, then
         topoSort(v, visited, T)
   done
   pop and print all elements from the stack in reverse order


```



## Code

### Python Implementation

```python

from collections import defaultdict

class Graph:

    def __init__(self,n):

        self.graph = defaultdict(list)

        self.N = n

    def addEdge(self,m,n):

        self.graph[m].append(n)

    def visit(self,n,visited,T):

        visited[n] = True

        for i in self.graph[n]:

            if visited[i] == False:

                self.visit(i,visited,T)

        T.insert(0,n)

    def topological_sort(self):

        visited = [False]*self.N

        T =[]

        for v in range(self.N):

            if visited[v] == False:

                self.visit(v,visited,T)

        print(T[::-1])

graph = Graph(5)
graph.addEdge(0,1)
graph.addEdge(0,3)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(2,4)
graph.addEdge(3,4)

print("Topological Sort:  ")

graph.topological_sort()



```



## Time Complexity


Time Complexity of the implementation is O(V+E),
    where V is the number of vertices and E is the number of edges in the graph.


## Space Complexity

Space complexity of O(V) needed for the stack.

## Sources
    

- [Topological sort - Tutorialspoint](https://www.tutorialspoint.com/Topological-Sorting/)
