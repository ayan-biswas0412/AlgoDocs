# Single source shortest paths Bellman-Ford algorithm

The Bellman-Ford algorithm solves the single source shortest-paths problem in the general case in which edge weights may be negative. The Bellman-Ford algorithm returns a boolean value indicating whether or not there is a negative-weight cycle that is reachable from the source. If there is such a cycle, the algorithm indicates that no solution exists. If there is no such cycle, the algorithm produces the shortest paths and their weights.

## Algorithm

```
INITIALIZE-SINGLE-SOURCE : Initializes the distance attribute to INFINITE and parent attribute to NULL for every vertex, and for the given source the distance is set to 0 and the parent is set to NULL.
RELAX                    : Given a edge, it updates the distance attribute of the destination vertex by comparing with the distance of source vertex and weight of the given edge.

```

## Pseudocode

```
Bellman-Ford algorithm
    G=(V,E)         : G is the given directed graph which have V number of vertices and E number of edges
    w : E->R        : w is the weight function which maps the weight of the each edge to the real values

    Node attributes
        Node        : x is an arbitrary node in the graph
        x.p         : The pointer which point to the parent node of x
        x.d         : The shortest distance of a vertex from the source vertex

    Edge attributes
        Edge        : (u,v) is an arbitrary edge composed of two nodes u and v
        source      : The vertex where the edge starts(here it is u)
        destination : The vertex where the edge ends(here it is v)
        w(u,v)      : The weight of the edge (u,v)

    INITIALIZE-SINGLE-SOURCE(G,s)
        for each vertex v belongs to G.V
            v.d=INFINITE
            v.p=NULL
        s.d=0
    
    RELAX(u,v,w)
        if v.d > u.d + w(u,v)
            v.d= u.d + w(u,v)
            v.p=u
        

    BELLMAN-FORD(G,w,s)
        INITIALIZE-SINGLE-SOURCE(G,s)
        for i=1 to |G.V| -1
            for each edge (u,v) belongs to G.E
                RELAX(u,v,w)
        for each edge (u,v) belongs to G.E
            if v.d > u.d + w(u,v)
                return FALSE
        return TRUE

```

## Code

### C++ Implementation

```cpp
#include<iostream>
#include<list>
using namespace std;
#define INFINITE 999999
class Node
{
public:
    char data;
    int distance;
    Node* parent;
    Node(char val)
    {
        data=val;
    }
};
class Edge
{
public:
    Node* source;
    Node* destination;
    int weight;
    Edge(Node* temp_u,Node* temp_v,int w_el)
    {
        source=temp_u;
        destination=temp_v;
        weight=w_el;
    }
};
class Graph
{
private:
    list<Node*> node_list;
    list<Edge*> edge_list;
    bool flag_negative_weight_cycle;
    Node* find_node_in_list(char val)
    {
        Node* temp=NULL;
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            if((*i)->data == val)
            {
                temp=*i;
                break;
            }
        }
        return temp;
    }
    void initialize_single_source(Node* temp)
    {
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp_v=*i;
            temp_v->distance=INFINITE;
            temp_v->parent=NULL;
        }
        temp->distance=0;
    }
    void relax_edge(Edge* ptr)
    {
        Node* temp_u=ptr->source;
        Node* temp_v=ptr->destination;
        if(temp_v->distance > (temp_u->distance + ptr->weight))
        {
            temp_v->distance=temp_u->distance + ptr->weight;
            temp_v->parent=temp_u;
        }
    }
    bool graph_bellman_ford(Node* temp)
    {
        initialize_single_source(temp);
        for(int i=0;i<(node_list.size() -1);i++)
        {
            for(auto j=edge_list.begin();j!=edge_list.end();j++)
            {
                relax_edge(*j);
            }
        }
        for(auto k=edge_list.begin();k!=edge_list.end();k++)
        {
            Edge* ptr=*k;
            Node* temp_u=ptr->source;
            Node* temp_v=ptr->destination;
            if(temp_v->distance > (temp_u->distance + ptr->weight))
            {
                return false;
            }
        }
        return true;
    }
    void graph_print_path(Node* temp)
    {
        if(temp->parent==NULL)
        {
            cout<<temp->data<<"("<<temp->distance<<")";
        }
        else
        {
            graph_print_path(temp->parent);
            cout<<"-->"<<temp->data<<"("<<temp->distance<<")";
        }
    }

public:
    void push_edge(char val_u,char val_v,int w_el)
    {
        Node* temp_u=NULL;
        Node* temp_v=NULL;
        if(node_list.empty()==true)
        {
            temp_u=new Node(val_u);
            temp_v=new Node(val_v);
            node_list.push_back(temp_u);
            node_list.push_back(temp_v);
            edge_list.push_back(new Edge(temp_u,temp_v,w_el));
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
                //both the nodes are already created and are found in the temp_u, temp_v variables
            }
            edge_list.push_back(new Edge(temp_u,temp_v,w_el));
        }
    }
    void bellman_ford(char val)
    {
        Node* temp=find_node_in_list(val);
        flag_negative_weight_cycle=graph_bellman_ford(temp);
        if(flag_negative_weight_cycle==true)
        {
            cout<<"No negative weight cycle exists"<<endl;
        }
        else
        {
            cout<<"Negative weight cycle exists"<<endl;
        }
    }
    void print_path(char val)
    {
        if(flag_negative_weight_cycle==true)
        {
            Node* temp=find_node_in_list(val);
            graph_print_path(temp);
        }
        else
        {
            cout<<"No single source shortest path available"<<endl;
        }
        
    }
};
int main()
{
    Graph obj;
    obj.push_edge('s','t',6);
    obj.push_edge('s','y',7);

    obj.push_edge('t','x',5);
    obj.push_edge('t','y',8);
    obj.push_edge('t','z',-4);

    obj.push_edge('x','t',-2);

    obj.push_edge('y','x',-3);
    obj.push_edge('y','z',9);

    obj.push_edge('z','s',2);
    obj.push_edge('z','x',7);
    
    obj.bellman_ford('s');
    cout<<endl;
    obj.print_path('z');
    return 0;
}

```

## Time Complexity

The time complexity of Bellman-Ford algorithm is O(VE).

## Space Complexity

The space complexity is O(V).

## Sources
    
- [Book-Introduction to Algorithms by CLRS](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)