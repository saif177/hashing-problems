def countSubArraySym(arr, k):
    def dist(pair):
       return pair[1] - pair[0]

    n = len(arr)
    smallest = None

    #step.1 calculate pre-fix sum
    pre_fix = [arr[0]]
    for i in range(1, n):
        pre_fix.append(pre_fix[i-1] + arr[i])
    
    #step.2 find sub-array between i and 0
    for i in range(n):
        if pre_fix[i] == k:
            if smallest is None or dist(smallest) > i:
                smallest = (i, 0)
    
    #step.3 Check subarrays between indexes i and j
    hm = {}
    for i in range(n):
        diff = pre_fix[i] - k
        if diff in hm:
            if smallest is None or dist(smallest) > dist((i, hm[diff] + 1)):
                # trick 1: pair has to be (i, j+1) and not (i,j)
                smallest = (i, hm[diff] + 1)
        hm[pre_fix[i]] = i

    return smallest

print(countSubArraySym([3,  6,   2,   8,   9,   2], 25))