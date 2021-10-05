# Quick Sort
It follows a divide and conquer paradigm. We usually use Recursion in quicksort implementation. In each recursive call, a pivot is chosen, then the array is partitioned in such a way that all the elements less than pivot lie to the left and all the elements greater than pivot lie to the right.
After every call, the chosen pivot occupies its correct position in the array which it is supposed to as in a sorted array.

## Algorithm

```
We are given with an input array
STEP 1 --> Choose pivot, here we are choosing the last element as our pivot
STEP 2 --> Now partition the array as per pivot
           Keep a partitioned index say p and initialize it to -1
           Iterate through every element in the array except the pivot
           If an element is less than the pivot element then increment p and swap the elements at index p with the element at index i.
           Once all the elements are traversed, swap pivot with element present at p+1 as this will the same position as in the sorted array
           Now return the pivot index
STEP 3 -->Once partitioned, now make 2 calls on quicksort
          One from beg to p-1
          Other from p+1 to n-1

```

## Pseudocode

```
/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

```



## Code

### C++ Implementation

```cpp

int partition (int arr[], int low, int high) 
{ 
    int pivot = arr[high]; // pivot 
    int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
  
    for (int j = low; j <= high - 1; j++) 
    { 
        // If current element is smaller than the pivot 
        if (arr[j] < pivot) 
        { 
            i++; // increment index of smaller element 
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return (i + 1); 
} 
  
/* The main function that implements QuickSort 
arr[] --> Array to be sorted, 
low --> Starting index, 
high --> Ending index */
void quickSort(int arr[], int low, int high) 
{ 
    if (low < high) 
    { 
        /* pi is partitioning index, arr[p] is now 
        at right place */
        int pi = partition(arr, low, high); 
  
        // Separately sort elements before 
        // partition and after partition 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 

```



### Python Implementation

```python
def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]
      
    # This loop runs till start pointer crosses 
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
          
        # Increment the start pointer till it finds an 
        # element greater than  pivot 
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        # Decrement the end pointer till it finds an 
        # element less than pivot
        while array[end] > pivot:
            end -= 1
          
        # If start and end have not crossed each other, 
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    # Returning end pointer to divide the array into 2
    return end
      
# The main function that implements QuickSort 
def quick_sort(start, end, array):
      
    if (start < end):
          
        # p is partitioning index, array[p] 
        # is at right place
        p = partition(start, end, array)
          
        # Sort elements before partition 
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
```




## Time Complexity

The time complexity of the above algorithm is  O(nlogn).


## Space Complexity

The algorithm runs in constant space O(logn).

## Sources
    

- [Quick Sort - GeeksforGeeks](https://www.geeksforgeeks.org/quick-sort/)