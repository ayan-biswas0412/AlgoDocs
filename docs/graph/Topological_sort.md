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