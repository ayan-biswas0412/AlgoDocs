# Bubble Sort

Bubble sort is based on that if you compare every pair posible in an array you can find the position of each in one in increasing or decreasing order.

## Algorithm

```
Step 1 − Compare forst pair of array
Step 2 − If the first one is bigger than the second one, swap their values
Step 3 − Go to next pair
Step 4 − Repeat until list is sorted
```

## Pseudocode

```
procedure bubble sort 

    list  : array of items
    n     : size of list

    for i = 1 to n - 1
      
        for j = 1 to n - i - 1
            
            if list[j] > list[j + 1]
                swap listS[j] and list[j + 1]
            end if

        end for
  
    end for

end procedure
```

## Code

### Python Implementation

```python
def bubble_sort(array):
    for outer in range(len(array) - 1):
        for inner in range(len(array) - 1 - outer):
            if array[inner] > array[inner + 1]:
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
    return array
```

## Time Complexity

The time complexity of the above algorithm is O(n^2).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Selection Sort - Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)