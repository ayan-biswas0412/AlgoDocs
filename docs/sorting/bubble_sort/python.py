def bubble_sort(array):
    """
    Bubble sort recieves an unordered array which sorts by using a swap
    subroutine, the main idea is to check all consecutive pairs possible
    in the array and determine if they should be swapped, if you do this
    eventually you will reach an ordered array.

    Meaning that is we have an array of N elements, then we need to compare
    all of its N^2 possible pairs, meaning that this algorithm will always 
    take O(N^2) time
    """
    for outer in range(len(array) - 1):
        for inner in range(len(array) - 1 - outer):
            if array[inner] > array[inner + 1]:
                # This is a one liner swap
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
    return array


if __name__ == "__main__":
    array = [5,8,3,6,1,2,0,4,7]
    result = bubble_sort(array)
    print("The array %s becomes %s after bubble sort" % (array, result))
