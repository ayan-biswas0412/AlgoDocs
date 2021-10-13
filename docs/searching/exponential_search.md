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
