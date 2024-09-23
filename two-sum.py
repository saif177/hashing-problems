
def twoSum(arr, target) :
    mp = dict()

    for i in range(len(arr)):
        remain = target - arr[i]
        if remain in mp:
            return [mp[remain], i]
        mp[arr[i]] = i  
    return []


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
