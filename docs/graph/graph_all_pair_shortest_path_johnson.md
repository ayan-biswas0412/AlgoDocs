# All pairs shortest paths Johnson algorithm
```
To find all pairs shortest paths for sparse graphs we can use Johnson's algorithm. Johnson's algorithm uses the technique of reweighting, which works as follows. If all edge weights w in a graph G=(V,E) are nonnegative, we can find shortest paths between all pairs of vertices by running Dijkstra's algorithm once from each vertex. If G has negative-weight edges but no negative-weight cycles, we can simply compute a new set of nonnegative edge weights that allows us to use the same method. The new set of edge weights w' must satisfy two important properties:
    1. For all pairs of vertices u,v belongs to V, a path p is a shortest path from u to v using weight function w if and only if p is also a shortest path from u to v using weight function w'.
    2. For all edges (u,v), the new weight w'(u,v) is nonnegative.
```

## Algorithm

```

Bellman-Ford algorithm : Finds if there are some negative-weight cycle present in the given graph and during the process the reweighting is also done.
Dijkstra's algorithm   : Computes the shortest path starting from a given vertex as source.
Johnson algorithm      : Compute G' from G, by inserting a new node s, which is a dummy node basically and w(s,v)=0 is set for all vertex v belongs to G. Then Bellman-Ford is run on the graph G to check if there are any negative-weight cycle. If there are no negative-weight cycle then each of the edges are reweighted and the weight function w' is generated. Then from each vertex Dijkstra algorithm is run and the shortest distances for each of the vertices are stored.

```

## Pseudocode
```

G=(V,E) is the given directed graph with weight function w, which has V number of vertice and E number of edges.
w: E-> R               : w is the weight funciton of the given directed graph G.
w'                     : w' is the weight function generated after reweighting all the edges in G.
(u,v)                  : It is an arbitrary edge starting from u and ending at v.
G.Adj(u)               : Adjacency list of the vertex u.
delta(s,v)             : s is the dummy source node which is made at the begining of Johnson algorithm. delta(s,v) is the shortest path distance from s to any arbitrary vertex v.
h(u)                   : u is an arbitrary vertex and h() is a function which helps to calculate the weight of edge (u,v).

Node attributes
        Node        : x is an arbitrary node in the graph
        x.p         : The pointer which point to the parent node of x
        x.d         : The shortest distance of vertex x from source vertex s
        h(x)        : It is the function which stroes the shortest distance of x, after running the Bellman-Ford algorithm subroutine

    Edge attributes
        Edge        : (u,v) is an edge composed of two nodes u and v
        source      : The vertex where the edge starts, here it is  u
        destination : The vertex where the edge ends, here it is v


INTIALIZE-SINGLE-SOURCE(G,s)
    for each vertex v belongs to G.V
        v.d=0
        v.p=NIL
    s.d=0

RELAX(u,v,w)
    if v.d > u.d + w(u,v)
        v.d=u.d + w(u,v)
        v.p=u

BELLMAN-FORD(G,w,s)
    INITIALIZE-SINGLE-SOURCE(G,s)
    for i=1 to |G.V| - 1
        for each edge (u,v) belongs to G.E
            RELAX(u,v,w)
    for each edge (u,v) belongs to G.E
        if v.d > u.d + w(u,v)
            return FALSE
    return TRUE

DIJKSTRA(G,w,s)
    INITIALIZE-SINGLE-SOURCE(G,s)
    S=0
    Q=G.V
    while Q!=Empty
        u=EXTRACT-MIN(Q)
        S=S U {u}
        for each vertex v belongs to G.Adj[u]
            RELAX(u,v,w)


JOHNSON(G,w)
    compute G', where G'.V=G.V U {S}
        G'.E=G.E U {(s,v) : v belongs to G.V}, and 
        w(s,v)=0 for all v belongs to G.V
    if BELLMAN-FORD(G',w,s)==FALSE
        print "the input graph contains a negative-weight cycle"
    else
        for each vertex v belongs to G'.V
            set h(v) to the value of delta(s,v) computed by the Bellman-Ford algorithm
        for each edge (u,v) belongs to G'.E
            w'(u,v)=w(u,v) + h(u) - h(v)
        let D be a new nxn matrix
        for each vertex u belongs to G.V
            run DIJKSTRA(G,w',u) to compute delta'(u,v) for all v belongs to G.V
            for each vertex v belongs to G.v
                D[u][v]=delta'(u,v) + h(v) - h(u)
        return D

```
## Code

### C++ Implementation

```cpp
#include<iostream>
#include<iomanip>
#include<map>
#include<list>
#include<set>
#include<vector>
using namespace std;
#define INFINITE 999999
class Node
{
public:
    int data;               //node data
    int distance;           //distance from a source vertex
    Node* parent;           //parent in that shortest path
    int h_weight;           //the h(u) or h(v) function defined in CLRS for reweighting the edges
    bool is_in_adjlist;     //whether a node has edges from it or not
    Node(int val)
    {
        data=val;
        is_in_adjlist=false; //initially it is false
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
class Node_with_weight
{
public:
    Node* vertex;
    int weight;
    Node_with_weight(Node* temp,int w_el)
    {
        vertex=temp;
        weight=w_el;
    }
};
class Comapare_nodes                        //only to make the adjlist more presentable while printing
{
public:
    bool operator()(Node* temp_u,Node* temp_v)
    {
        return (temp_u->data < temp_v->data);
    }
};
class Compare_node_distance                //used as the comaparison function in the set
{
public:
    bool operator()(Node* temp_u,Node* temp_v)
    {
        return (temp_u->distance < temp_v->distance);
    }
};
class Graph
{
private:
    int no_of_vertices;
    Node* dummy;                   //the dummy node from which initially the bellman-ford algorithm is run
    bool flag_negative_weight_cycle;
    map<Node*,list<Node_with_weight*>,Comapare_nodes> adjlist;
    list<Node*> node_list;
    list<Edge*> edge_list;
    multiset<Node*,Compare_node_distance> node_set;
    vector<vector<int>> johnson_sol;
    vector<vector<int>> shortest_path;

    Node* find_node_in_list(int val)
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
    void relax_edge_bellman_ford(Edge* ptr)     //relax function for bellman-ford algorithm
    {
        Node* temp_u=ptr->source;
        Node* temp_v=ptr->destination;
        if(temp_v->distance > (temp_u->distance + ptr->weight))
        {
            temp_v->distance=temp_u->distance + ptr->weight;
            temp_v->parent=temp_u;
        }
    }
    void relax_edge_dijkstra(Node* temp_u, Node_with_weight* ptr)   //relax function for dijkstra algorithm
    {
        Node* temp_v=ptr->vertex;
        if(temp_v->distance > (temp_u->distance + ptr->weight))
        {
            node_set.erase(temp_v);
            temp_v->distance=temp_u->distance + ptr->weight;
            temp_v->parent=temp_u;                               
            node_set.insert(temp_v);
        }
    }
    bool graph_bellman_ford(Node* temp)
    {
        initialize_single_source(temp);
        for(int i=0;i<(node_list.size() -1);i++)
        {
            for(auto j=edge_list.begin();j!=edge_list.end();j++)
            {
                relax_edge_bellman_ford(*j);
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
    void graph_dijkstra(Node* temp)
    {
        initialize_single_source(temp);
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            Node* temp_u=*i;
            node_set.insert(temp_u);
        }
        while(node_set.empty()!=true)
        {
            Node* temp_u=*(node_set.begin());
            node_set.erase(temp_u);
            if(temp_u->is_in_adjlist==true)
            {
                list<Node_with_weight*> l=(adjlist.find(temp_u))->second;
                for(auto i=l.begin();i!=l.end();i++)
                {
                    Node_with_weight* ptr=*i;
                    relax_edge_dijkstra(temp_u,ptr);
                }
            }
        }
    }

public:
    Graph(int n)
    {
        no_of_vertices=n;
    }
    void push_edge(int val_u,int val_v,int w_el)
    {
        Node* temp_u=NULL;
        Node* temp_v=NULL;
        if(node_list.empty()==true)
        {
            temp_u=new Node(val_u);
            temp_v=new Node(val_v);
            node_list.push_back(temp_u);
            node_list.push_back(temp_v);

            adjlist[temp_u].push_back(new Node_with_weight(temp_v,w_el));
            temp_u->is_in_adjlist=true;
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
            adjlist[temp_u].push_back(new Node_with_weight(temp_v,w_el));
            temp_u->is_in_adjlist=true;
            edge_list.push_back(new Edge(temp_u,temp_v,w_el));
        }
    }
    void show_graph()
    {
        for(auto i=adjlist.begin();i!=adjlist.end();i++)
        {
            Node* temp_u=i->first;
            cout<<temp_u->data<<"-> ";
            list<Node_with_weight*> temp_list=i->second;
            for(auto j=temp_list.begin();j!=temp_list.end();j++)
            {
                Node* temp_v=(*j)->vertex;
                cout<<"("<<temp_v->data<<") ";
            }
            cout<<endl;
        }
    }
    void johnson_algorithm()                                                                    //CLRS JOHNSON
    {
        int dist[no_of_vertices][no_of_vertices];
        int path[no_of_vertices][no_of_vertices];
        dummy=new Node(0);                                                                      //the node s, the dummy node
        dummy->is_in_adjlist=true;
        for(auto i=node_list.begin();i!=node_list.end();i++)
        {
            adjlist[dummy].push_back(new Node_with_weight(*i,0));                               //making G', where G'.V= G.V U {s}
            edge_list.push_back(new Edge(dummy,*i,0));                                          //G'.E= G.E U {(s,v) : v belongs to G.V} and w(s,v)=0 for all v belongs to G.V
        }
        if(graph_bellman_ford(dummy)==false)
        {
            cout<<"The given graph contains negative weight cycle"<<endl;
        }
        else
        {
            for(auto i=node_list.begin();i!=node_list.end();i++)
            {
                Node* temp=*i;
                temp->h_weight=temp->distance;                                                //for each vertex v belongs to G'.V, h(v)= delta(s,v) computed by bellman-ford algorithm
            }
            for(auto j=edge_list.begin();j!=edge_list.end();j++)
            {
                Edge* ptr=*j;                                                                  //for each edge (u,v) belongs to G'.E
                ptr->weight=ptr->weight + ptr->source->h_weight - ptr->destination->h_weight; // w'(u,v) = w(u,v) + h(u) - h(v)
                list<Node_with_weight*> temp_list=(adjlist.find(ptr->source)->second);
                for(auto h=temp_list.begin();h!=temp_list.end();h++)
                {
                    if((*h)->vertex->data == ptr->destination->data)
                    {
                        (*h)->weight=ptr->weight;
                    }
                }
            }
            for(auto i=node_list.begin();i!=node_list.end();i++)
            {
                Node* temp_u=*i;
                graph_dijkstra(temp_u);
                for(auto j=node_list.begin();j!=node_list.end();j++)
                {
                    Node* temp_v=*j;
                    dist[temp_u->data -1][temp_v->data -1]=temp_v->distance + temp_v->h_weight - temp_u->h_weight;
                    if(temp_v->parent!=NULL)
                    {
                        path[temp_u->data -1][temp_v->data -1]=temp_v->parent->data;            //d[u][v]=delta'(u,v) + h(v) - h(u)
                    }
                    else
                    {
                        path[temp_u->data -1][temp_v->data -1]=0;
                    }
                }
            }
        }
        for(int i=0;i<no_of_vertices;i++)
        {
            vector<int> vec;
            vector<int> res;
            for(int j=0;j<no_of_vertices;j++)
            {
                if(i==j)
                {
                    vec.push_back(0);
                    res.push_back(0);
                }
                else
                {
                    vec.push_back(dist[i][j]);
                    res.push_back(path[i][j]);
                }
            }
            johnson_sol.push_back(vec);
            shortest_path.push_back(res);
        }
    }
    void show_johnson_solution_matrix()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                cout<<setw(5)<<johnson_sol[i][j];
            }
            cout<<endl;
        }
    }
    void show_johnson_path_matrix()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                cout<<setw(5)<<shortest_path[i][j];
            }
            cout<<endl;
        }
    }
    void print_path(int i,int j)
    {
        if(shortest_path[i][j]-1==i)
        {
            return;
        }
        else
        {
            print_path(i,shortest_path[i][j]-1);
            cout<<shortest_path[i][j]<<"->";
        }
    }
    void show_all_pair_shortest_path_solution()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                if(i!=j)
                {
                    cout<<"The shortest path from vertex "<<i+1<<"->vertex "<<j+1<<" is"<<endl;
                    cout<<"("<<i+1<<"->";
                    print_path(i,j);
                    cout<<j+1<<")"<<" with path weight= "<<johnson_sol[i][j]<<endl;
                }
            }
        }
    }

};
int main()
{
    int v,e;
    int val_u,val_v,w_el;
    cout<<"Enter the no of vertices in the directed graph= ";
    cin>>v;
    cout<<"Enter the no of edges in the directed graph= ";
    cin>>e;
    Graph obj(v);
    cout<<"Now enter the edges as source vertex, destination vertex, weight of the edge"<<endl;
    for(int i=0;i<e;i++)
    {
        cin>>val_u;
        cin>>val_v;
        cin>>w_el;
        obj.push_edge(val_u,val_v,w_el);
    }
    cout<<"The adjacency list representation of the given directed graph"<<endl;
    obj.show_graph();
    cout<<"Implementing Johson's algorithm to find all pair shortest path"<<endl;
    obj.johnson_algorithm();
    cout<<"Showing the Johnson's solution matrix"<<endl;
    obj.show_johnson_solution_matrix();
    cout<<"Showing the shortest path matrix"<<endl;
    obj.show_johnson_path_matrix();
    cout<<"Showing all the shortest path weight with path information between all pairs of vertices"<<endl;
    obj.show_all_pair_shortest_path_solution();

    return 0;
}
```

## Time Complexity

The time complexity of Johnson algorithm is O(|V|^2 log(|V|) + |V||E|)

## Space Complexity

The space complexity is O(|V|^2).

## Sources
    
- [Book-Introduction to Algorithms by CLRS](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)