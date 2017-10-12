"Quicksort: sort in place, return nothing"
def quickSort_inPlace(array, low = None, high = None):
    low = 0 if low is None else low
    high = len(array) if high is None else high
    if high - low <= 1:
        return
    else:
        i = low
        for j in range(low, high-1):
            if array[j] <= array[high-1]:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[i], array[high-1] = array[high-1], array[i]
        quickSort_inPlace(array, low, i)
        quickSort_inPlace(array, i+1, high)

"Quicksort: return the sorted array"
def quickSort_return(array):
    if len(array) <= 1:
        return array
    else:
        pivot = [x for x in array if x == array[-1]]
        left = quickSort_return([x for x in array if x < pivot[0]])
        right = quickSort_return([x for x in array if x > pivot[0]])
        return left + pivot + right
