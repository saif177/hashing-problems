from collections import defaultdict
def subArrayXor(Arr, B):
    hash = defaultdict(int)
    pre = [Arr[0]]
    
    #step.1 calculate pre-fix xor for each element of Arr
    for i in range(1, len(Arr)):
        pre.append(pre[i-1] ^ Arr[i])

    #step.2 find pre[i] ^ B and get total occurance 
    count = 0
    for i in pre:
        
        if i == B :
            count += 1

        xor = B^i

        if xor == B:
            count += 1
        
        if xor in hash:
            count += hash[xor]
        
        hash[i] += 1

    return count

print(subArrayXor([4, 2, 2, 6, 4], 6))