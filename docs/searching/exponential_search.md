# Exponential Search 
 
Exponential search allows for searching through a sorted and unbounded list for a specified value or key. It is also known as galloping or doubling search.

## Algorithm 

```
Step 1: Find the range within which the element or "key" is present. 
Step 2: Using binary search, search for the key within the range found in step 1.

```

## Pseudocode 

```
procedure exponential_search
       A : array of numbers 
       key : element to be found or searched for 
       start : lower bound
       end : upper bound
       
       if (A[0]==key)
         return 0
       if ((end - start) <= 0)
           return NOT_FOUND 
       end if 

       i = 1
       while (i < (end - start)) do
            if A[i] < key
                i = i*2
            end if    
       done
       return binary_search(A, i/2, i, key)
end procedure       
```
## Code

### C implementation
```c
#include <stdio.h>
int binarySearch(int arr[], int, int, int); 
int exponentialSearch(int arr[], int n, int x) 
{ 
    // If x is present at firt location itself 
    if (arr[0] == x) 
        return 0; 

    // Find range for binary search by 
    // repeated doubling 
    int i = 1; 
    while (i < n && arr[i] <= x) 
        i = i*2; 

    //  Call binary search for the found range. 
    return binarySearch(arr, i/2, min(i, n), x); 
} 

// A recursive binary search function. It returns 
// location of x in  given array arr[l..r] is 
// present, otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{ 
    if (r >= l) 
    { 
        int mid = l + (r - l)/2; 

        // If the element is present at the middle 
        // itself 
        if (arr[mid] == x) 
            return mid; 

        // If element is smaller than mid, then it 
        // can only be present n left subarray 
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid-1, x); 

        // Else the element can only be present 
        // in right subarray 
        return binarySearch(arr, mid+1, r, x); 
    } 

    // We reach here when element is not present 
    // in array 
    return -1; 
} 

int main(void) 
{ 
   int arr[] = {2, 3, 4, 10, 40}; 
   int n = sizeof(arr)/ sizeof(arr[0]); 
   int x = 10; 
   int result = exponentialSearch(arr, n, x); 
   (result == -1)? printf("Element is not present in array") 
                 : printf("Element is present at index %d", 
                                                    result); 
   return 0; 
} 
```

### C++ implementation

```cpp
int exponentialSearch(int A[], int start, int end, int key){
    if(A[0]==key)
     return 0; 
    if((end - start) <= 0)
      return -1;  //not found or invalid location
    int i = 1; // as 2^0 = 1  
    while(i < (end - start)){
         if(A[i] < key)
            i *= 2; //doubling i
         else
            break; //when A[i] crosses the key element    
    }
   return binarySearch(A, i/2, i, key); //search key within the range
}
```

### Java implementation

```java
    static int expSearch(int array[], int n, int searchValue) {
      //if value is at position one
      if(array[0] == searchValue) {
       return 0;
      }
      //find the range for the binary search
      int i = 1;
      while (i < n && array[i] <= searchValue) {
       i = i * 2;
      }
      //now call the binary search
      return Arrays.binarySearch(array, (i / 2), Math.min(i, n), searchValue);
    }
```

## Time Complexity

The time complexity of Exponential Search is O(log n), where n is the size of the given array.

## Space Complexity

The algorithm runs in constant space O(1).

## Sources

- [Exponential Search - GeeksforGeeks](https://www.geeksforgeeks.org/exponential-search/)
- [Exponential Search - Tutorialspoint](https://www.tutorialspoint.com/Exponential-Search)
- [Exponential Search - Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)
