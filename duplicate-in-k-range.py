from collections import Counter

def checkDuplicate(arr, k):
    if not arr :
        return False
    hash = {}
    for i in range(len(arr)):
        
        if arr[i] in hash and i - hash[arr[i]] <= k:
            return True
        hash[arr[i]] = i

    return False

     

print(checkDuplicate([1,2,3,4,1,2,3,4], 3))
print(checkDuplicate([1,2,3,1,2,3,4], 3))
print(checkDuplicate([1,2,3,4,5], 3))
print(checkDuplicate([1,2,3,4,4], 3))
