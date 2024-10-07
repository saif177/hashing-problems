from collections import defaultdict

def countSubArraySym(arr, k):
    count = 0
    n = len(arr)
    
    #step.1 calculate pre-fix sum
    pre_fix = [arr[0]]
    for i in range(1, n):
        pre_fix.append(pre_fix[i-1] + arr[i])
    
    #step.2 cound pre_fix[i] == k
    for i in pre_fix:
        if i == k:
            count += 1
    
    #step.3 count pre_fix[i] - pre_fix[j] == k
    hash = defaultdict(int)
    for j in pre_fix:
        count += hash[j - k]
        hash[j] += 1
    
    return count



print(countSubArraySym([10, 2, -2, -20, 10], -10))