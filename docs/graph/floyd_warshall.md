# Floyd Warshall

The Floyd-Warshall's algorithm is a graph analysis algorithm for finding shortest paths in a weighted, directed graph. A single execution of the algorithm will find the shortest paths between all pairs of vertices.

## Algorithm

```
We initialize the solution matrix same as the input graph matrix as a first step. Then we update the solution matrix by considering all vertices as an intermediate vertex. The idea is to one by one pick all vertices and updates all shortest paths which include the picked vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair (i, j) of the source and destination vertices respectively, there are two possible cases. 
1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is. 
2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]
```

## Pseudocode

```
procedure floyd_warshall
   n = no of vertices
   A = matrix of dimension n*n
   
    for k = 1 to n
       for i = 1 to n
           for j = 1 to n
                Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
    return A    
end procedure
```

## Code

## C Implementation
```C
// defining the number of vertices
void printMatrix(int matrix[20][20],int n);

// Implementing floyd warshall algorithm
void floydWarshall(int cost[20][20],int n) {
  int matrix[20][20], i, j, k;

  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      matrix[i][j] = cost[i][j];

  // Adding vertices individually
  for (k = 0; k < n; k++) {
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        if (matrix[i][k] + matrix[k][j] < matrix[i][j])
          matrix[i][j] = matrix[i][k] + matrix[k][j];
      }
    }
  }
  printMatrix(matrix,n);
}

// Function to print the output matrix
void printMatrix(int matrix[20][20],int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (matrix[i][j] == 999)
        printf("%4s", "INF");
      else
        printf("%4d", matrix[i][j]);
    }
    printf("\n");
  }
}

// Main function
int main() 
{
  int cost[20][20],i,j,n;
  printf("enter the number of vertices");
  scanf("%d",&n);
  printf("enter the matrix\n");
  for(i=0;i<n;i++)
   {
    for(j=0;j<n;j++)
      {
      scanf("%d",&cost[i][j]);
      }
   }
  floydWarshall(cost,n);
}
```


### C++ Implementation

```C++
#define nV 4
#define INF 999

void printMatrix(int matrix[][nV]);

// Implementing floyd warshall algorithm
void floydWarshall(int graph[][nV]) {
  int matrix[nV][nV], i, j, k;

  for (i = 0; i < nV; i++)
    for (j = 0; j < nV; j++)
      matrix[i][j] = graph[i][j];

  // Adding vertices individually
  for (k = 0; k < nV; k++) {
    for (i = 0; i < nV; i++) {
      for (j = 0; j < nV; j++) {
        if (matrix[i][k] + matrix[k][j] < matrix[i][j])
          matrix[i][j] = matrix[i][k] + matrix[k][j];
      }
    }
  }
  printMatrix(matrix);
}

void printMatrix(int matrix[][nV]) {
  for (int i = 0; i < nV; i++) {
    for (int j = 0; j < nV; j++) {
      if (matrix[i][j] == INF)
        printf("%4s", "INF");
      else
        printf("%4d", matrix[i][j]);
    }
    printf("\n");
  }
}

int main() {
  int graph[nV][nV] = {{0, 3, INF, 5},
             {2, 0, INF, 4},
             {INF, 1, 0, INF},
             {INF, INF, 2, 0}};
  floydWarshall(graph);
}
```


## Time Complexity

The time complexity of the above algorithm is O(n<sup>3</sup>).

## Space Complexity

The space complexity of the Floyd-Warshall algorithm is O(n<sup>2</sup>).

## Sources
    
- [Floyd-Warshall - Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Floyd-Warshall - geekforgeeks](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)
