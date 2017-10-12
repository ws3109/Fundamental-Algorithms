import random
import time

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



def test():
    numNumbers = 100000
    maxNumber = 100000
    array = [random.randint(1, maxNumber) for _ in range(numNumbers)]
    answer = sorted(array)
    assert answer == mergeSort(array)

test()
