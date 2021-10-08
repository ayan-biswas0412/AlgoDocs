# All pairs shortest paths Floyd-Warshall algorithm

The floyd-Warshall algorithm can be considered as a dynamic programming algorithm, which initially assumes that there are no negative weight cycles present in the given directed graph. The Floyd-Warshall algorithm considers the intermediate vertices of a shortest path, where an intermediate vertex of a simple path p={v1,v2,v3,...,vl} is any vetex of p other than v1 or vl, that is, any vertex in the set {v2,v3,v4,...,vl-1}.
## Algorithm

```
The Floyd-Warshall algorithm exploits a relationship between path p and shortest paths from i to j with all intermediate vertices in the set {1,2,3,...,k-1}. The relationship depends on whether or not k is an intermediate vertex of path p.

If k is not an intermediate vertex of path p, then all intermediate vertices of path p are in the set {1,2,3,...,k-1}. Thus, a shortest path from vertex i to vertex j with all intermediate vertices in the set {1,2,3...,k-1} is also a shortest path from i to j with all intermediate vertices in the set {1,2,3,...,k-1}.

If k is an intermediate vertex of path p, then we decompose p into i-->path p1-->k-->path p2-->j,p1 is the shortest path from i to k with all intermediate vertices in the set {1,2,3,...,k-1}. Because k is not an intermediate vertex of path p1, all intermediate vertices of p1 are in the set {1,2,3,...,k-1}. Therefore p1 is a shortest path from i to k with all intermediate vertices in the set {1,2,3,...,k-1}. Similarly, p2 is the shortest path from vertex k to vertex j with all the intermediate vertices in the set {1,2,3,...,k-1}.
```

## Pseudocode
```
ADJOINT_MATRIX: It is a square matrix which contains the edge weights of an arbitrary edge (i,j) which have weight w, at the ith row and jth column of the matrix.
n             : It is the length of the rows and columns of ADJOINT_MATRIX
dist[n][n]    : It is the matrix, which initially copies all the elements from ADJOINT_MATRIX and then the Floyd-Warshall algorithm works on it and computes the all pairs shortest paths, it computes the shortest path for an arbitrary vertex i to j and saves the result in the ith row and jth column of dist[n][n] matrix.
path[n][n]    : It is the martrix which initially takes value of the source vertex, at ith row and jth column which is i, for the edges which have different source and destination, as going from one vertex to itself means going no where. If there is no edge from i to j then the entry in the ith row and jth column will be -1. The path matrix is updated in the Floyd-Warshall algorithm and records the parents of one vertex in the simple path formed when we have considered an arbitrary vertex i as source.

    FLOYD-WARSHALL(ADJOINT_MATRIX)
        dist[n][n]
        path[n][n]
        for i=1 to n
            for j=1 to n
                dist[i][j]=ADJOINT_MATRIX[i][j]
                if(i==j)
                    path[i][j]=0;
                elseif dist[i][j]!=INFINITE
                    path[i][j]=i;
                else
                    path[i][j]=-1;
        for k=1 to n
            for i=1 to n
                for j=1 to n
                    if((dist[i][j] > (dist[i][k]+dist[k][j])) && (dist[i][k]!=INFINITE && dist[k][j]!=INFINITE))
                        dist[i][j]=dist[i][k]+dist[k][j]
                        path[i][j]=path[k][j]

```
## Code

### C++ Implementation

```cpp
#include<iostream>
#include<iomanip>
#include<vector>
using namespace std;
#define INFINITE 999999
class Graph
{
private:
    int no_of_vertices;
    vector<vector<int>> adj_matrix;
    vector<vector<int>> floyd_warshall_sol;
    vector<vector<int>> shortest_path;
public:
    Graph(int v)
    {
        no_of_vertices=v;
        for(int i=0;i<no_of_vertices;i++)
        {
            vector<int> vec;
            for(int j=0;j<no_of_vertices;j++)
            {
                if(i==j)
                {
                    vec.push_back(0);
                }
                else
                {
                    vec.push_back(INFINITE);
                }
            }
            adj_matrix.push_back(vec);
        }
    }
    void push_edge(int val_u,int val_v,int w_el)
    {
        adj_matrix.at(val_u-1).at(val_v-1)=w_el;
    }
    void show_graph()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                if(adj_matrix[i][j]==INFINITE)
                {
                    cout<<setw(5)<<"INF";
                }
                else
                {
                    cout<<setw(5)<<adj_matrix[i][j];
                }
            }
            cout<<endl;
        }
    }
    void floyd_warshall_solution()
    {
        int dist[no_of_vertices][no_of_vertices];
        int path[no_of_vertices][no_of_vertices];
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                dist[i][j]=adj_matrix[i][j];
                if(i==j)
                {
                    path[i][j]=0;
                }
                else if(dist[i][j]!=INFINITE)
                {
                    path[i][j]=i+1;
                }
                else
                {
                    path[i][j]=-1;
                }
            }
        }
        for(int k=0;k<no_of_vertices;k++)
        {
            for(int i=0;i<no_of_vertices;i++)
            {
                for(int j=0;j<no_of_vertices;j++)
                {
                    if((dist[i][j] > (dist[i][k]+dist[k][j])) && (dist[i][k]!=INFINITE && dist[k][j]!=INFINITE))
                    {
                        dist[i][j]=dist[i][k]+dist[k][j];
                        path[i][j]=path[k][j];
                    }
                }
            }
        }
        for(int i=0;i<no_of_vertices;i++)
        {
            vector<int> res;
            vector<int> p;
            for(int j=0;j<no_of_vertices;j++)
            {
                res.push_back(dist[i][j]);
                p.push_back(path[i][j]);
            }
            floyd_warshall_sol.push_back(res);
            shortest_path.push_back(p);
        }
    }
    void show_floyd_warshall_solution()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                cout<<setw(5)<<floyd_warshall_sol[i][j];
            }
            cout<<endl;
        }
    }
    void show_shortest_path()
    {
        for(int i=0;i<no_of_vertices;i++)
        {
            for(int j=0;j<no_of_vertices;j++)
            {
                if(shortest_path[i][j]==0)
                {
                    cout<<setw(5)<<"NIL";
                }
                else
                {
                    cout<<setw(5)<<shortest_path[i][j];
                }
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
                if(i!=j && (shortest_path[i][j]!=-1))
                {
                    cout<<"The shortest path from vertex "<<i+1<<"->vertex "<<j+1<<" is"<<endl;
                    cout<<"("<<i+1<<"->";
                    print_path(i,j);
                    cout<<j+1<<")"<<" with path weight= "<<floyd_warshall_sol[i][j]<<endl;
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
    cout<<"The adjacency matrix representation of the given directed graph"<<endl;
    obj.show_graph();
    obj.floyd_warshall_solution();
    cout<<"The all pair shortest path solution is"<<endl;
    obj.show_floyd_warshall_solution();
    cout<<"Showing the shortest path matrix"<<endl;
    obj.show_shortest_path();
    cout<<"Showing all the shortest path weight with path information between all pairs of vertices"<<endl;
    obj.show_all_pair_shortest_path_solution();
    return 0;
}

```

## Time Complexity

The time complexity of Floyd-Warshall algorithm is O(|V|^3).

## Space Complexity

The space complexity is O(|V|^2).

## Sources
    
- [Book-Introduction to Algorithms by CLRS](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)