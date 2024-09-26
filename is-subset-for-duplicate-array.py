from collections import Counter
def isSubSet(arr, subset):
    counter = Counter(arr)

    for i in subset:
        if i in counter and counter.get(i) >= 1:
            counter[i] -= 1
        else :
            return False
    return True


arr = [1,2,3,4,5,6,8,8,7]
subArr = [1,8,3,8]

print(isSubSet(arr, subArr))