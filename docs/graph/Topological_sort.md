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

### C++ Implementation

```C++

#include <iostream>
#include <list>
#include <stack>
using namespace std;

class Graph {
    // No. of vertices'
    int V;
    // Pointer to an array containing adjacency listsList
    list<int>* adj;
    // A function used by topologicalSort
    void topologicalSortUtil(int v, bool visited[],
                             stack<int>& Stack);
 
public:
    Graph(int V);
    // function to add an edge to graph
    void addEdge(int v, int w);
    // prints a Topological Sort of
    // the complete graph
    void topologicalSort();
};
 
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
 
void Graph::addEdge(int v, int w)
{
    // Add w to v’s list.
    adj[v].push_back(w);
}
 
// A recursive function used by topologicalSort
void Graph::topologicalSortUtil(int v, bool visited[],
                                stack<int>& Stack)
{
    // Mark the current node as visited.
    visited[v] = true;
    // Recur for all the vertices
    // adjacent to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            topologicalSortUtil(*i, visited, Stack);
    // Push current vertex to stack
    // which stores result
    Stack.push(v);
}
 
// The function to do Topological Sort.
// It uses recursive topologicalSortUtil()
void Graph::topologicalSort()
{
    stack<int> Stack;
    // Mark all the vertices as not visited
    bool* visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
    // Call the recursive helper function
    // to store Topological
    // Sort starting from all
    // vertices one by one
    for (int i = 0; i < V; i++)
        if (visited[i] == false)
            topologicalSortUtil(i, visited, Stack);
    // Print contents of stack
    while (Stack.empty() == false) {
        cout << Stack.top() << " ";
        Stack.pop();
    }
}
 
int main()
{
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    cout << "Following is a Topological Sort of the given "
            "graph \n";
    g.topologicalSort();
    return 0;
}

```

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
### Java Implementation

```java

public class TopologicalSort {

    static Set<Integer> recStac;
    static Set<Integer> visited;
    static Stack<Integer> res;
    static ArrayList[] adj;
    public static int[] solve(int A, int[][] B) {
        recStac = new HashSet();
        visited = new HashSet();
        res = new Stack();
        adj = new ArrayList[A+1];
        
        for(int i=0; i<= A; i++){
            adj[i] = new ArrayList();
        }
        
        for(int i=0; i<B.length; i++){
            adj[B[i][0]].add(B[i][1]);
        }
        boolean ans = false;
        for(int i=1; i<=A;i++){
            // if(adj[i].size() <= 0) continue;
            if(visited.contains(i)) continue;
            ans = dfs(i);
            if(ans == true){
                return new int[0];
            }
        }
        
        int[] result = new int[A];
        int i=A-1;
        while(!res.isEmpty()){
            result[i--] = res.pop();
        }
        return result;
    }
    
    public static boolean dfs(int cur){
        if(recStac.contains(cur)){
            return true;
        }
        if(visited.contains(cur)){
            return false;
        }
        
        visited.add(cur);
        recStac.add(cur);
        PriorityQueue<Integer> minheap = new PriorityQueue();
        minheap.addAll(adj[cur]);
        while(!minheap.isEmpty()){
            int next = (int)minheap.poll();
            if(dfs(next)){
                return true;
            }
        }
        res.push(cur);
        recStac.remove(cur);
        return false;
    }
    
    public static void main(String[] args){
      int no_of_nodes = 6;
      int[][] directed_edges = { {6, 3}, {6, 1}, {5, 1}, {5, 2}, {3, 4}, {4, 2} };
      System.out.printf(Arrays.toString(solve(no_of_nodes, directed_edges)));
    }
    
}

```
### Javascript Implementation

```javascript

topologicalSortHelper(node, explored, s) {
   explored.add(node);
   this.edges[node].forEach(n => {
      if (!explored.has(n)) {
         this.topologicalSortHelper(n, explored, s);
      }
   });
   s.push(node);
}

topologicalSort() {
   let s = new Stack(this.nodes.length);
   let explored = new Set();

   this.nodes.forEach(node => {
      if (!explored.has(node)) {
         this.topologicalSortHelper(node, explored, s);
      }
   });

   while (!s.isEmpty()) {
      console.log(s.pop());
   }
}

let g = new Graph();
g.addNode("A");
g.addNode("B");
g.addNode("C");
g.addNode("D");
g.addNode("E");
g.addNode("F");
g.addNode("G");

g.addDirectedEdge("A", "C");
g.addDirectedEdge("A", "B");
g.addDirectedEdge("A", "D");
g.addDirectedEdge("C", "D");
g.addDirectedEdge("D", "E");
g.addDirectedEdge("E", "F");
g.addDirectedEdge("B", "G");

g.topologicalSort();

```

## Time Complexity


Time Complexity of the implementation is O(V+E),
    where V is the number of vertices and E is the number of edges in the graph.


## Space Complexity

Space complexity of O(V) needed for the stack.

## Sources
    

- [Topological sort - Tutorialspoint](https://www.tutorialspoint.com/Topological-Sorting/)
