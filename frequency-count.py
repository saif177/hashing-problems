#https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/?ref=lbp

def countFreq(arr) :
    mp = dict()
    for i in range(len(arr)):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else :
            mp[arr[i]] = 1
    
    print(mp)


arr = [1,2,4,1,5,3,6,3,6,3,2,3,6,8,6,25]

countFreq(arr)