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


## Time Complexity

The time complexity of the above algorithm is O(nlogn).

## Space Complexity

The algorithm runs in constant space O(n).

## Sources

- [Merge Sort - Tutorials Point](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)
- [Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
