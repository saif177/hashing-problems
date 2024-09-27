
def countPairs(arr, target):
    resCount = 0
    myHash = dict()
    for num in arr:
        remind = target - num
        if remind in myHash:
            resCount += myHash[remind]

        myHash[num] = myHash.get(num, 0) + 1
        
    return resCount



arr = [1,1,1,1]
target = 2

ans = countPairs(arr, target)

print(ans)