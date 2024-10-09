from collections import defaultdict

def countKDifference(nums, k):
     #step.1 initialized hash with num frequency
    hash = defaultdict(int)

    #step.2 count nums[i] - k and k + nums[i] 
    # to count k diff value 
    count = 0
    for i in range(len(nums)):
        count += hash[k + nums[i]]
        count += hash[nums[i] - k]
        hash[nums[i]] += 1
    return count


print(countKDifference([1,2,2,1], 1))