def binary_search(array, low, high, target):
    """
    Parameters
    ----------
    array : list[int] 
        Description of parameter `x`.
    low : int
        Index for bottom of list
    high: int
        Index for top of list
    target: int
        the element we are seaching


    Returns
    -------
    int
        Index in which your target is located in array

    Binary search is recursive algorithm the works with a sorted
    array, it starts of the middle of the array, if the current value
    is less than target then its at the left of the array, and if it
    is bigger then is at the right.

    This recursive procedure means that if we have an array of N elements
    then in the worst case scenario we are finding the target at O(logN)
    since we are dividing the array in two with every conditional.
    """
    if high >= low:

        mid = (high + low) // 2

        if array[mid] == target:
            return target
        elif array[mid] > target:
            return binary_search(array, low, mid - 1, target)
        else:
            return binary_search(array, mid + 1, high, target)

if __name__ == "__main__"
    array = [1,2,3,4,5,6,7,8,9,10,11]
    target = 10
    result = binary_search(array, 0, len(array - 1), target)
    print("Your target %s is at the %s index" % (target, result))

