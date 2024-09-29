from collections import defaultdict

def countSubArraySum(arr, Sum):
    res = 0
    currSum = 0
    myHash = defaultdict(lambda: 0)
    for i in range(len(arr)):
        
        currSum += arr[i]

        if currSum == Sum :
            res += 1
        
        if currSum - Sum in  myHash:
            res += myHash[currSum - Sum]

        myHash[currSum] += 1

    return res 


arr =  [10, 2, -2, -20, 10]  
Sum = -10 

ans = countSubArraySum(arr, Sum)

print(ans)