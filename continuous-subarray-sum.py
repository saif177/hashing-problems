from collections import defaultdict

def continueSubArraySum(nums, k):
    hash = { 0 : -1 }
    pre_fix = 0
    
    for i, n in enumerate(nums):
        pre_fix += n
        remain = pre_fix % k

        if remain not in hash:
            hash[remain] = i
        elif i - hash[remain] > 1:
            return True
        
    return False 

print(continueSubArraySum([23,2,4,6,7], 6))