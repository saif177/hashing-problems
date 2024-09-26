def isSubSet(arr, subset):
    set1 = set(arr)

    for i in subset:
        if i not in set1:
            return False
    return True


arr = [1,2,3,4,5,6,7]
subArr = [1,5,3]

print(isSubSet(arr, subArr))