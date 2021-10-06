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

### C++ Implementation

```cpp
void bubbleSort(int arr[], int n)
{
   int i, j;
   bool swapped;
   for (i = 0; i < n-1; i++)
   {
     swapped = false;
     for (j = 0; j < n-i-1; j++)
     {
        if (arr[j] > arr[j+1])
        {
           swap(&arr[j], &arr[j+1]);
           swapped = true;
        }
     }
 
     // if no two elements were swapped by inner loop, then break
     if (swapped == false)
        break;
   }
}
```
### C Implementation

```C
void bubbleSort(int arr[], int n)
{
   int i, j, temp;
   for (i = 0; i < n-1; i++)     
       // Last i elements are already in place  
       for (j = 0; j < n-i-1; j++)
           if (arr[j] > arr[j+1])
	   {
	      temp = arr[j];
	      arr[j] = arr[j+1];
	      arr[j+1]=temp;
	   }
}
```
### Java Implementation

```java
void bubbleSort(int arr[], int n)
    {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++)
        {
            swapped = false;
            for (j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
 
            if (swapped == false)
                break;
        }
    }
```    

### Python Implementation

```python
def bubble_sort(array):
    for outer in range(len(array) - 1):
        for inner in range(len(array) - 1 - outer):
            if array[inner] > array[inner + 1]:
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
    return array
```

### Go Implementation

```go
func bubbleSort(array []int) []int {
	for i := 0; i < len(array) - 1; i++ {
		for j := 0; j < len(array) - 1 - i; j++ {
			array[i], array[i+1] = array[i+1], array[i]
		}
	}
	return array
}
```
### Javascript Implementation

```js
let bubbleSort = (array) => {
	for(int i = 0; i < array.length(); i++) {
		for(int j = 0; j < array.length - 1 - i; j++) {
			let temp = array[j];
			array[j] = array[j+1];
			array[j+1] = array[j];
		}
	}
	return array;
}
```

## Time Complexity

The time complexity of the above algorithm is O(n^2).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Bubble Sort - Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)
- [Bubble Sort - GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/)
