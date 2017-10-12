import random
import time

"Python style radix sort"
def radixSort(array, base = 10):
    for i in range(32):
        array = sorted(array, key = lambda x: (x / base ** i) % base)
    return array

def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = mergeSort(array[0:mid])
        right = mergeSort(array[mid:])
        return merge(left, right)

def merge(arrayA, arrayB):
    i, j = 0, 0
    result = []
    for _ in range(len(arrayA) + len(arrayB)):
        if j == len(arrayB) or i < len(arrayA) and arrayA[i] <= arrayB[j]:
            result.append(arrayA[i])
            i = i + 1
        elif i == len(arrayA) or j < len(arrayB) and arrayB[j] <= arrayA[i]:
            result.append(arrayB[j])
            j = j + 1
    return result

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

def test():
    numNumbers = 100000
    maxNumber = 100000
    array = [random.randint(1, maxNumber) for _ in range(numNumbers)]
    answer = sorted(array)
    for f in [mergeSort, quickSort_return, quickSort_inPlace, radixSort, sorted]:
        start = time.clock()
        sorted_array = f(array)
        if f == quickSort_inPlace:
            sorted_array = array
        end = time.clock()
        print(str(f), end - start, sorted_array == answer)

test()
