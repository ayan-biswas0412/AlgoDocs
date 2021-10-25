# Topological Sorting
# Topological Sorting is ordering of vertices or nodes such if there is an edge between (u,v) then u should come before v in topological sorting. Topological sort is possible only for Directed Acyclic Graph(DAG). If there is a cycle in graph, then there won’t be any possibility for Topological Sort.
# Please note that there can be more than one solution for topological sort.

Let’s pick up node 30 here.

Node 30 depends on node 20 and node 10.
Node 10 depends on node 20 and node 40.
Node 20 depends on node 40.

Hence node 10, node 20 and node 40 should come before node 30 in topological sorting.

This algorithm is a variant of Depth-first search. In depth first search, we first print the vertex and then go to its neighbours but  in case of topological sort, we don’t print vertex immediately instead we push it to the Stack.

In topological sorting, we will have a temporary stack. We are not going to print the vertex immediately, we first recursively call topological sorting for all its neighbour vertices, then push it to a stack. We will print stack once we are done with recursive topolgical sorting.


# Code
    ## JAVA implementation
    package org.arpit.java2blog;
 
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
 
public class TopologicalSort
{ 
    Stack<Node> stack;
 
    public TopologicalSort() {
        stack=new Stack<>();
    }
    static class Node
    {
        int data;
        boolean visited;
        List<Node> neighbours;
 
        Node(int data)
        {
            this.data=data;
            this.neighbours=new ArrayList<>();
 
        }
        public void addneighbours(Node neighbourNode)
        {
            this.neighbours.add(neighbourNode);
        }
        public List<Node> getNeighbours() {
            return neighbours;
        }
        public void setNeighbours(List<Node> neighbours) {
            this.neighbours = neighbours;
        }
        public String toString()
        {
            return ""+data;
        }
    }
 
    // Recursive toplogical Sort
    public  void toplogicalSort(Node node)
    {
        List<Node> neighbours=node.getNeighbours();
        for (int i = 0; i < neighbours.size(); i++) {
            Node n=neighbours.get(i);
            if(n!=null && !n.visited)
            {
                toplogicalSort(n);
                n.visited=true;
            }
        }
        stack.push(node);
    }
 
    public static void main(String arg[])
    {
 
        TopologicalSort topological = new TopologicalSort();
        Node node40 =new Node(40);
        Node node10 =new Node(10);
        Node node20 =new Node(20);
        Node node30 =new Node(30);
        Node node60 =new Node(60);
        Node node50 =new Node(50);
        Node node70 =new Node(70);
 
        node40.addneighbours(node10);
        node40.addneighbours(node20);
        node10.addneighbours(node30);
        node20.addneighbours(node10);
        node20.addneighbours(node30);
        node20.addneighbours(node60);
        node20.addneighbours(node50);
        node30.addneighbours(node60);
        node60.addneighbours(node70);
        node50.addneighbours(node70);
 
        System.out.println("Topological Sorting Order:");
        topological.toplogicalSort(node40);
 
        // Print contents of stack
        Stack<Node> resultStack=topological.stack;
        while (resultStack.empty()==false)
            System.out.print(resultStack.pop() + " ");
    }
 
}
 

   
    ...
# Sources https://java2blog.com/topological-sort-java/#Topological_Sort_Algorithm
# Conclusion (if any)




