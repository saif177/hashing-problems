def maxDistanceBetweenNums(arr):
    max_distance = 0
    myHash = {}
    for i in range(len(arr)):
        if arr[i] not in myHash:
            myHash[arr[i]] = i
        else:
            curr_dist = i - myHash[arr[i]] 
            max_distance = max(curr_dist, max_distance)
            
    return max_distance


arr = [ 3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

ans = maxDistanceBetweenNums(arr)

print(ans)