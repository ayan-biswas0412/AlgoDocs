# Strongly connected components-Kosaraju Algorithm

A directed graph is strongly connected if there is a path between all pairs of vertices. In Kosaraju algorithm Depth First Search is run twice on the given Directed graph and the
vertices of each tree in the depth first forest formed are the separate strongly connected components.

## Algorithm

```
Step 1 - The given directed graph is G, DFS(G) is run to calculate the finishing times of each of the vertices.
Step 2 - The tranpose of graph G is computed.
Step 3 - DFS() is run on the G transpose graph.
Step 4 - The vertices of each tree in the depth first forest are the strongly conncected component.

```

## Pseudocode

```
procedure strongly conncected components Kosaraju algorithm
    G   : The given directed graph
    u   : An arbitary vertex of the given graph G
    u.f : It is the attribute of the vertex u, which is called as finishing time for vertex u
    DFS : Depth first search, where a search is initiated from a particular vertex and it continues along the depth first manner, and returns back to the 
          first initiated vertex, when there is no vertex to discover in the depth along

    STRONGLY-CONNECTED-COMPONENTS(G)
    1.call DFS(G) to compute the finishing times of u.f for each vertex u
    2.compute G transpose
    3.call DFS(G transpose), but int the main loop of DFS, consider the vertices in order of decreasing u.f (as computed in the line 1)
    4.output the vertices of each tree in the depth-first forest formed in line 3 as a separate strongly conncted component
end procedure

```

## Code

### C++ Implementation

```cpp
#include<iostream>
#include<map>
#include<list>
using namespace std;
enum color{WHITE,GRAY,BLACK};
int time;
class Node
{
public:
    char data;
    int color;
    int discovered;
    int finished;
    bool is_in_adjlist_g; //to know whether this node has any edges from it in the given graph, if not, then we can skip the recursive dfs_visit_g call while visiting this node
    bool is_in_adjlist_t; //to know whether this node has any edges from it in the transpose of the given graph, if not, then we can skip the recursive dfs_visit_t call while visiting this node
    Node* parent_in_g; //parent of a node while doing the first dfs visit
    Node* parent_in_t; //parent of a node while doing the second dfs visit
    Node(char el)
    {
        data=el;
        is_in_adjlist_g=false;
        is_in_adjlist_t=false;
    }
};
class Compare_nodes                     //used only for representing the graph in a sorted manner, on the terminal
{
public:
    bool operator()(Node* temp_u,Node* temp_v)
    {
        return (temp_u->data < temp_v->data);
    }
};
class Graph
{
private:
    map<Node*,list<Node*>,Compare_nodes> adjlist_g; //adjacency list of the given graph
    map<Node*,list<Node*>,Compare_nodes> adjlist_t; //adjacency list of the transpose of the given graph

    list<Node*> node_list;
    list<Node*> finishing_time_list;       //using this list to store the nodes in decreasing order of the finishig time while doing the first dfs
    Node* find_node_in_list(char val)
    {
        Node* temp=NULL;
        for(auto iter=node_list.begin();iter!=node_list.end();iter++)
        {
            if((*iter)->data == val)
            {
                temp=*iter;
                break;
            }
        }
        return temp;
    }
    void dfs_visit_g(Node* temp_u)
    {
        time=time+1;
        temp_u->discovered=time;
        temp_u->color=GRAY;
        if(temp_u->is_in_adjlist_g==true)
        {
            list<Node*> l=(adjlist_g.find(temp_u))->second;
            for(auto it=l.begin();it!=l.end();it++)
            {
                Node* temp_v=*it;
                if(temp_v->color==WHITE)
                {
                    temp_v->parent_in_g=temp_u;
                    dfs_visit_g(temp_v);
                }
            }
        }
        temp_u->color=BLACK;
        time=time+1;
        temp_u->finished=time;
        finishing_time_list.push_front(temp_u);
    }
    void dfs_visit_t(Node* temp_u)
    {
        time=time+1;
        temp_u->discovered=time;
        temp_u->color=GRAY;
        cout<<temp_u->data<<" ";
        if(temp_u->is_in_adjlist_t==true)
        {
            list<Node*> l=(adjlist_t.find(temp_u))->second;
            for(auto it=l.begin();it!=l.end();it++)
            {
                Node* temp_v=*it;
                if(temp_v->color==WHITE)
                {
                    temp_v->parent_in_t=temp_u;
                    dfs_visit_t(temp_v);
                }
            }
        }
        temp_u->color=BLACK;
        time=time+1;
        temp_u->finished=time;
    }

public:
    void push_edge(char val_u,char val_v)
    {
        Node* temp_u=NULL;
        Node* temp_v=NULL;
        if(node_list.empty()==true)
        {
            temp_u=new Node(val_u);
            temp_v=new Node(val_v);
            node_list.push_back(temp_u);
            node_list.push_back(temp_v);

            adjlist_g[temp_u].push_back(temp_v); //pushing the directed edge of the given graph
            temp_u->is_in_adjlist_g=true;

            adjlist_t[temp_v].push_back(temp_u); //pushing the reverse directed edge of these particular vertices
            temp_v->is_in_adjlist_t=true;
        }
        else
        {
            temp_u=find_node_in_list(val_u);
            temp_v=find_node_in_list(val_v);
            if(temp_u==NULL && temp_v==NULL)
            {
                temp_u=new Node(val_u);
                temp_v=new Node(val_v);
                node_list.push_back(temp_u);
                node_list.push_back(temp_v);
            }
            else if(temp_u!=NULL && temp_v==NULL)
            {
                temp_v=new Node(val_v);
                node_list.push_back(temp_v);
            }
            else if(temp_u==NULL && temp_v!=NULL)
            {
                temp_u=new Node(val_u);
                node_list.push_back(temp_u);
            }
            else
            {
                //both the nodes are already created and are found in the variables temp_u, temp_v
            }
            adjlist_g[temp_u].push_back(temp_v);
            temp_u->is_in_adjlist_g=true;

            adjlist_t[temp_v].push_back(temp_u);
            temp_v->is_in_adjlist_t=true;
        }
    }
    void show_graph_data()
    {
        cout<<"Adjacency-list representation of the graph:"<<endl;
        for(auto i=adjlist_g.begin();i!=adjlist_g.end();i++)
        {
            Node* temp_u=i->first;
            list<Node*> j=i->second;
            cout<<temp_u->data<<"-->";
            for(auto k=j.begin();k!=j.end();k++)
            {
                Node* temp_v=*k;
                cout<<temp_v->data<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
        cout<<"Adjacency-list representation of the tranpose graph:"<<endl;
        for(auto i=adjlist_t.begin();i!=adjlist_t.end();i++)
        {
            Node* temp_u=i->first;
            list<Node*> j=i->second;
            cout<<temp_u->data<<"-->";
            for(auto k=j.begin();k!=j.end();k++)
            {
                Node* temp_v=*k;
                cout<<temp_v->data<<" ";
            }
            cout<<endl;
        }
    }
    void dfs_g()
    {
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp=*i;
            temp->color=WHITE;
            temp->parent_in_g=NULL;
        }
        time=0;
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp=*i;
            if(temp->color==WHITE)
            {
                dfs_visit_g(temp);
            }
        }
    }
    void dfs_t()
    {
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp=*i;
            temp->color=WHITE;
            temp->parent_in_t=NULL;
        }
        time=0;
        for(auto i=finishing_time_list.begin();i!=finishing_time_list.end();i++)
        {
            Node* temp=*i;
            if(temp->color==WHITE)
            {
                dfs_visit_t(temp);
                cout<<endl;
            }
        }
    }
    void show_dfs_result()
    {
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp=*i;
            cout<<temp->data<<"("<<temp->discovered<<"/"<<temp->finished<<")"<<" ";
        }
    }
    void strongly_connected_components()
    {
        dfs_g();
        cout<<"The strongly connected components are:"<<endl;
        dfs_t();
    }
};
int main()
{
    Graph obj;
    obj.push_edge('a','b');

    obj.push_edge('b','c');
    obj.push_edge('b','f');
    obj.push_edge('b','e');

    obj.push_edge('c','d');
    obj.push_edge('c','g');

    obj.push_edge('d','c');
    obj.push_edge('d','h');

    obj.push_edge('e','a');
    obj.push_edge('e','f');

    obj.push_edge('f','g');

    obj.push_edge('g','f');
    obj.push_edge('g','h');

    obj.push_edge('h','h');


    obj.show_graph_data();
    cout<<endl;
    obj.strongly_connected_components();
    return 0;
}
```

## Time Complexity

The time complexity of the above algorithm is O(V+E).

## Space Complexity

The algorithm runs in O(V) space.

## Sources
    
- [Book-Introduction to Algorithms by CLRS](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)