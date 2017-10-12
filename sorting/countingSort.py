import random

def countingSort(array):
    count = [0 for _ in range(max(array)+1)]
    for num in array:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    result = [0 for _ in range(len(array))]
    for i in range(len(array) - 1, -1, -1):
        result[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
    return result

def test():
    numNumbers = 1000000
    maxNumber = 100000
    array = [random.randint(1, maxNumber) for _ in range(numNumbers)]
    answer = sorted(array)
    assert countingSort(array) == answer

test()
