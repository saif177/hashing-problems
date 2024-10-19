def count4SumPairs(arr, k):
    n = len(arr)
    count = 0
    hash = {}

    #Step.1 Store reminder for target - (ar[i] + ar[j])
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            if pair_sum in hash:
                hash[pair_sum] += 1
            else:
                hash[pair_sum] = 1

    #Step.2 Find reminder of quadruplet
    for i in range(n):
        for j in range(i + 1, n):
            target_sum = k - (arr[i] + arr[j])
            if target_sum in hash:
                count += hash[target_sum]

    return count

print(count4SumPairs([1, 2, 3, 4, 5], 10)) 