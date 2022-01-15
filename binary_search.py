
def binary_search(array, x):
    start = 0
    end = len(array) - 1
    middle = 0
 
    while start <= end:
        middle = (end + start) // 2
        if array[middle] < x:
            start = middle + 1
        elif array[middle] > x:
            end = middle - 1
        else:
            return True
    return False
