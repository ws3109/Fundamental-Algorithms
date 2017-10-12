import random
import math
import time

def radixSort(array, base = 10):
    maxLen = int(math.log(max(array), base)) + 1
    for i in range(maxLen):
        bins = [[] for _ in range(base)]
        for number in array:
            bins[(number//base**i)%base].append(number)
        array = []
        for section in bins:
            array.extend(section)
    return array

def test():
    numNumbers = 100000
    maxNumber = numNumbers ** 2
    array = [random.randint(1, maxNumber) for _ in range(numNumbers)]
    answer = sorted(array)
    start = time.clock()
    assert radixSort(array) == answer
    end = time.clock()
    print(end - start)

test()
