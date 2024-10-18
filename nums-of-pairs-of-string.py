from collections import defaultdict
def countNumsofPairsOfString(nums, target):
    count=0
    hash = defaultdict(int)
    
    for num in nums:
        hash[num] += 1

    for num in hash:
        if target.startswith(num):
            remain = target.replace(num, '', 1)
            
            if num == remain:
                count += hash[num] * (hash[num] - 1)
            elif remain in hash:
                count += hash[remain] * hash[num]

    return count


print(countNumsofPairsOfString(["123","4","12","34"], "1234"))