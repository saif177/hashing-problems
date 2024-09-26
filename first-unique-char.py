from collections import Counter

def uniqueCharacter(s):

    myCount = Counter(s)
    for i in range(len(s)):
        char = myCount.get(s[i])
        if char == 1 :
            return i 

    return -1

s = "leetcode"
#s = "loveleetcode"
ans = uniqueCharacter(s)

print(ans)