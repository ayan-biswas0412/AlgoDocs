# Linear Search

Linear search is an algorithm the traverses an array from beggining to end sequentially in order to find the index of your element, meaning that in our best case scenario de target we are searching is the first element while the worst scenario is the last.

## Algorithm

```
Step 1 − Iterate over array
Step 2 − Compare current iteration with target
Step 3 − If Step 2 is true return index
```

## Pseudocode

```
procedure linear search 
    list  : array of items
    target: size of list

    for i = 1 to n - 1
        if list[i] == target
            return i
        end if
    end for
end procedure
```

## Code

### C Implementation

```C
int search(int array[], int n, int x) {
  
  // Going through array sequencially
  for (int i = 0; i < n; i++)
    if (array[i] == x)
      return i;
  return -1;
}
```

### C++ Implementation

```cpp  
// Linearly search x in arr[].  If x is present then return its location,  otherwise return -1
int search(int arr[], int size, int x)
{
    int i;
    for (i = 0; i < size; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
```

### Python Implementation

```python
def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index 
```

## Java Implementation

```java
    public int linear_search(int array[], int size, int key){
        for(int i=0; i<size; i++)
            if(array[i]==key)
                return i;
        return -1;
    }
```

## Javascript Implementation

```javascript
 function linear_search(array, key) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === key) 
    {
      return i;
    }
  }
  return -1;
}
```
## Golang Implementation

```golang
 func linearsearch(datalist []int, key int) bool {
	for _, item := range datalist {
		if item == key {
			return true
		}
	}
	return false
} 
```
## Time Complexity

The time complexity of the above algorithm is O(n).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Linear Search](https://en.wikipedia.org/wiki/Linear_search)
- [Linear Search - GeeksforGeeks](https://www.geeksforgeeks.org/linear-search/)
