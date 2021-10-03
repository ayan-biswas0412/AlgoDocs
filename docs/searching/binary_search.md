# Binary Search

Binary search is recursive algorithm the works with a sorted array, it starts of the middle of the array, if the current value is less than target then its at the left of the array, and if it is bigger then is at the right.

## Algorithm

```
Step 1 − Get the midpoint of your array
Step 2 − If your target is in the midpoint return it
Step 3 − If the value in the midpoint is lower than your target, use the the midpoint as high
Step 4 − If the value in the midpoint is greater than your target, use the midpoint as low
```

## Pseudocode

```
procedure binary_search 
    array : list
    low   : lower bound 
    high  : higher bound 
    target: number we are searching 
  
    if high >= low

        mid = floor((high + low) / 2)

        if array[mid] == target
            return mid
        else if array[mid] > target
            return binary_search(array, low, mid - 1, target)
        else
            return binary_search(array, mid + 1, high, target)
        end if

    end if
end procedure
```

## Code

### Python Implementation

```python
def binary_search(array, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            return binary_search(array, low, mid - 1, target)
        else:
            return binary_search(array, mid + 1, high, target)
```

## Time Complexity

The time complexity of the above algorithm is O(logN).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Binary Search - Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)