
def twoSum(arr, target) :
    mp = dict()

    for i in range(len(arr)):
        remain = target - arr[i]
        if remain in mp:
            return True
            #return [mp[remain], i]
        mp[arr[i]] = i  
    return False


nums = [0, -1, 2, -3, 1]
target = -2

print(twoSum(nums, target))
