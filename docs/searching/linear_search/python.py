def linear_search(array, target):
    """
    Linear search is an algorithm the traverses an array
    from beggining to end sequentially in order to find 
    the index of your element, meaning that in our 
    best case scenario de target we are searching is the
    first element while the worst scenario is the last.

    This means that if we have an array of N elements then
    it can take up to O(N) time to execute.
    """
    for index, element in enumerate(array):
        if element == target:
            return index 

if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    target = 4
    result = linear_search(array, target)
    print("Your target %s is in the %s index" % (target, result))
