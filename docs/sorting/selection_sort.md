# Selection Sort

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

## Algorithm

```
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted

```

## Pseudocode

```
procedure selection sort 
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
end procedure

```

## Code

### C++ Implementation

```cpp
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;
 
        // Swap the found minimum element with the first element
        swap(&arr[min_idx], &arr[i]);
    }
}
```

### C Implementation

```C
void selectionSort(int arr[], int n)
{
    int i, j, min, temp;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min])
            min = j;
 
        // Swap the found minimum element with the first element
        temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}
```

### Java Implementation

```Java
void selectionSort(int arr[])
{
    int i, j, min_index, temp, n;
    n = arr.length;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min_index = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_index])
            min_index = j;
 
        // Swap the found minimum element with the first element
        temp = arr[min_index];
        arr[min_index] = arr[i];
        arr[i] = temp;
    }
}
```

### Python Implementation

```python
def selectionSort(arr):
    n = len(arr)
 
    # One by one move boundary of unsorted subarray
    for i in range(n-1):
 
        # Find the minimum element in unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
 
        # Swap the found minimum element with the first element
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
```
### Javascript Implementation

```javascript
function selectionSort(arr,  n)
{
    var i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++)
        if (arr[j] < arr[min_idx])
            min_idx = j;
 
        // Swap the found minimum element with the first element
        var temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
```
### Golang Implemention
```Golang
func Selection_Sort(array[] int, size int) []int {
   var min_index int
   var temp int
   for i := 0; i < size - 1; i++ {
      min_index = i
      // Find index of minimum element
      for j := i + 1; j < size; j++ {
         if array[j] < array[min_index] {
            min_index = j
         }
      }
      temp = array[i]
      array[i] = array[min_index]
      array[min_index] = temp
   }
   return array
}
```
### Swift Implementation

```swift
func selectionSort(array: inout [Int]) {
    
    for currentIndex in array.indices {
        var minIndex = currentIndex
        
        for index in (currentIndex + 1)..<array.count {
            if(array[index] < array[minIndex]) {
                minIndex = index
            }
        }
        
        if (minIndex != currentIndex) {
            let temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        }
        
    }
}
```
### PHP Implementation
```PHP
function selectionSort($data)
{
    $n=count($data);
    $minIndex=null;     //the index of next min value or max value
    $temp=null;
 
    for($i=0; $i<$n-1; $i++)
    {
 
        $minIndex=$i;
        for($j=$i+1; $j<$n; $j++)
            if( $data[$j]<$data[$minIndex] ) //change the < to > for descending order
                $minIndex=$j; 
 
        //swap the current index of the outer loop with the next min value
        $temp=$data[$i];
        $data[$i]=$data[$minIndex];
        $data[$minIndex]=$temp;
    }
 
    return $data;
}
```
## Time Complexity

The time complexity of the above algorithm is O(n^2).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Selection Sort - Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)
- [Selection Sort - GeeksforGeeks](https://www.geeksforgeeks.org/selection-sort/)
