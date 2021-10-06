#  Insertion Sort
 The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

## Algorithm

```
Step 1: Iterate from arr[1] to arr[n] over the array. 
Step 2: Compare the current element (key) to its predecessor. 
Step 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

```

## Pseudocode

```
procedure insertion sort 
   A  : array of items
   n     : size of list

  INSERTION-SORT(A)
   for i = 1 to n
   	key ← A [i]
    	j ← i – 1
  	 while j > = 0 and A[j] > key
   		A[j+1] ← A[j]
   		j ← j – 1
   	End while 
   	A[j+1] ← key
  End for 

```

## Code

### C++ Implementation

```cpp

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

### C Implementation

```c

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
 
        /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

### Python Implementation

```python
def insertion_sort(array):  
  
        for i in range(1, len(array)):  
            key = array[i]  
  
            # Move elements of array[0..i-1], that are  
            # greater than key, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and key < array[j]:  
                array[j + 1] = array[j]  
                j -= 1  
            array[j + 1] = key  
        return array
```

### Javascript Implementation

```javascript
function insertionSort(arr, n) 
{   
    let i, key, j; 
    for (i = 1; i < n; i++)
    { 
        key = arr[i]; 
        j = i - 1; 
   
        //Move elements of arr[0..i-1], that are 
        //greater than key, to one position ahead 
        //of their current position //
        while (j >= 0 && arr[j] > key)
        { 
            arr[j + 1] = arr[j]; 
            j = j - 1; 
        } 
        arr[j + 1] = key; 
    } 
} 
```
### Java Implementation

```java
static void insertionSort(int arr[], int n){
        int i, key, j;
        for (i=0;i<n;i++){
            key = arr[i];
            j = i - 1;
        /* Move elements of arr[0..i-1], that are
        greater than key, to one position ahead
        of their current position */
            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
```

## Time Complexity

The time complexity of the above algorithm is O(n^2).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Insertion Sort - InterviewBit](https://www.interviewbit.com/tutorial/insertion-sort-algorithm/)
- [Insertion Sort - GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort/)
