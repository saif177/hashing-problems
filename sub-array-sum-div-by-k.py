from collections import defaultdict

def prefixArrayDivisByK(arr, k):
    n = len(arr)
    count = 0
    
    #step.1 calculate pre-fix sum
    pre_sum = [arr[0]]
    for i in range(1, n):
        pre_sum.append(pre_sum[i-1] + arr[i])
    
    #step.2 find pre-fix sum == k
    #commented because case is being handled below
    # for i in pre_sum:
    #     if i % k == 0:
    #         count += 1

    #step.3 find prefix % k 
    hash = defaultdict(lambda: 0)
    hash[0] = 1         
    
    for j in range(n):
        mod = pre_sum[j] % k 
        
        if mod == 0 :
            continue

        if mod < 0:
            mod += k
        
        if mod in hash:
            count += hash[mod]
        hash[mod] += 1

    return count

print(prefixArrayDivisByK([4,5,0,1], 5))


