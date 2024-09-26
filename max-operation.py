from collections import Counter

def minOperation(arr):
    if not arr:
        return 0
    numCount = list(Counter(arr).most_common(1).pop())
    return len(arr) - numCount[1] 

#arr = [12,4,5,3,5,6,3,6,3,22,41]
#arr = [1, 5, 2, 1, 3, 2, 1] 
arr = []
ans = minOperation(arr)
print(ans)