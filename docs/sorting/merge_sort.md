# Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Algorithm

```

Step 1 − if it is only one element in the list it is already sorted, return.

Step 2 − divide the list recursively into two halves until it can no more be divided.
Step 3 − merge the smaller lists into new list in sorted order.

```

## Pseudocode

```
procedure mergesort( var a as array )
   if ( n == 1 ) return a

   var l1 as array = a[0] ... a[n/2]
   var l2 as array = a[n/2+1] ... a[n]

   l1 = mergesort( l1 )
   l2 = mergesort( l2 )

   return merge( l1, l2 )
end procedure

procedure merge( var a as array, var b as array )
   var c as array
   while ( a and b have elements )
      if ( a[0] > b[0] )
         add b[0] to the end of c
         remove b[0] from b
      else
         add a[0] to the end of c
         remove a[0] from a
      end if
   end while
   
   while ( a has elements )
      add a[0] to the end of c
      remove a[0] from a
   end while
   
   while ( b has elements )
      add b[0] to the end of c
      remove b[0] from b
   end while
   
   return c	
end procedure
```

## Code

### C++ Implementation

```cpp

void mergeSort(int arr[], int l, int r)
{


    if (l < r) {

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}


```

### C Implementation

```C

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int i, j, k, n1, n2;
    n1 = m - l + 1;
    n2 = r - m;
  
    /* create temp arrays */
    int L[n1], R[n2];
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
  
    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
  
    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
  
/* l is for left index and r is right index of the
sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;
        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
```

### JavaScript Implementation
```javascript
function mergeSort(arr, l, r) {
  if (l >= r) {
    return;
  }
  var m = l + parseInt((r - l) / 2);
  mergeSort(arr, l, m);
  mergeSort(arr, m + 1, r);
  merge(arr, l, m, r);
}
```
### Java implementation

```java
void mergeSort(int arr[], int l, int r){
  if(r > l){
    int m = l + (r - l)/2;
    mergeSort(arr, l, m);
    mergeSort(arr, m+1, r);
    merge(arr, l, m, r);
  }
}
```
### Python implementation
```python 
def merge(arr1, arr2):
    arr3 = []
    while(len(arr1)>0 and len(arr2)>0):
        if(arr1[0]<arr2[0]):
            arr3.append(arr1[0])
            arr1.remove(arr1[0])
        else:
            arr3.append(arr2[0])
            arr2.remove(arr2[0])
    if(len(arr1)>0):
        arr3 = arr3 + arr1
    if(len(arr2)>0):
        arr3 = arr3 + arr2 
    return arr3   

def mergeSort(arr):
    if (len(arr) == 1):
        return arr
    else: 
        m = int(len(arr)/2)
        arr1 = mergeSort(arr[0:m])
        arr2 = mergeSort(arr[m:])
        return merge(arr1, arr2)
```
### OCaml implementation
```ocaml
let rec merge arr1 arr2 = 
  match (arr1, arr2) with
  | (a1::arr1A, a2::arr2A) -> 
      if a1 < a2 
      then a1::(merge arr1A arr2) 
      else a2::(merge arr1 arr2A) 
  | (arr1A, []) -> arr1A                                                            
  | ([], arr2A) -> arr2A 
;;


let rec mergeSort arr = 
  let m = (List.length arr) in 
  if m == 1 
  then arr
  else let (arr1, arr2) = listSplit arr (m/2)
    in merge (mergeSort arr1) (mergeSort arr2)
;;
```

## Time Complexity

The time complexity of the above algorithm is O(nlogn).

## Space Complexity

The algorithm runs in constant space O(n).

## Sources

- [Merge Sort - Tutorials Point](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)
- [Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
