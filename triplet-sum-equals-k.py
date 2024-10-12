def tripletSum(nums, k):
    if not nums or len(nums) < 3:
        return False
    
    n = len(nums)
    for i in range(n-1):
        hash = {}
        target = k - nums[i]
        for j in range(i+1, n):
            if target - nums[j] in hash:
                return [nums[i], nums[j], target - nums[j]]
            hash[nums[j]] = i
    return False

print(tripletSum([1, 4, 45, 6, 10, 8], 22))