'''
 
    Problem Statement : Detect Pattern of Length M Repeated K or More Times
    Link : https://leetcode.com/contest/weekly-contest-204/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
    Score : accepted
 
'''

def containsPattern(arr, m, k):
    arr_str = ''.join(map(str,arr))
    for i in range(0,len(arr)-m):   
        pat = ''.join(map(str,arr[i:i+m]))
        pat *= k     
        if(arr_str.count(pat)):
            return True
    return False

print(containsPattern([1,2,1,2,1,1,1,3], m = 2, k = 2))