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

### C++ Implementation

```C++
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
  
        // If the element is present at the middle
        // itself
        if (arr[mid] == x)
            return mid;
  
        // If element is smaller than mid, then
        // it can only be present in left subarray
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
  
        // Else the element can only be present
        // in right subarray
        return binarySearch(arr, mid + 1, r, x);
    }
  
    // We reach here when element is not
    // present in array
    return -1;
}
```

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
### Golang Implementation
```golang
func binarySearch(needle int, haystack []int) bool {

	low := 0
	high := len(haystack) - 1

	for low <= high{
		median := (low + high) / 2

		if haystack[median] < needle {
			low = median + 1
		}else{
			high = median - 1
		}
	}

	if low == len(haystack) || haystack[low] != needle {
		return false
	}

	return true
}
```

## Java Implementation
```java
binarySearch(int arr[], int low, int high,int data){
	while(l<=h) {
			int m = (l+h)/2;
			if(data>arr[m]) {
				l=m+1;
			} else if(data<arr[m]) {
				h=m-1;
			} else {
				System.out.println(m);
				return;
			}
		}
		System.out.println(-1); //not found
}
```

## JavaScript Implementation
```javascript
function binarySearch(Arr, key){
    let start = 0;
    let end = Arr.length - 1;
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        if (Arr[mid] === key) {
            return mid;
        } 
        else if (Arr[mid] < key) {
            start = mid + 1;
        }
         else {
            end = mid - 1;
        }
    }
    return -1;
}
```

### C Implementation
```c
int binarySearch(int arr[], int left, int right, int search)
{
    while (left <= right) {
        int mid = left + (right - left) / 2;
  
        if (arr[mid] == search)
            return mid;
  
        if (arr[mid] < search)
            left = mid + 1;
  
        else
            right = mid - 1;
    }
    return -1;
```

## Swift Implementation
```swift
func binarySearch(array: [Int], lhs: Int, rhs: Int, target: Int) -> Int? {
    if rhs >= lhs {
        let mid = Int((rhs + lhs) / 2)

        if array[mid] == target {
            return mid
        } else if array[mid] > target {
            return binarySearch(array: array, lhs: lhs, rhs: mid - 1, target: target)
        } else{
            return binarySearch(array: array, lhs: mid + 1, rhs: rhs, target: target)
        }
    } else {
        return nil
    }
}
```

## Time Complexity

The time complexity of the above algorithm is O(logN).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Binary Search - Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [Binary Search - geekforgeeks](https://www.geeksforgeeks.org/binary-search/)
