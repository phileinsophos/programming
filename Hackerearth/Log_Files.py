'''
        Problem Statement : Log files
        Link : https://www.hackerearth.com/challenges/competitive/data-structures-and-algorithms-coding-contest-jan-21/algorithm/log-searching-247e417e/
        Score : partially accepted - 87
'''

def CountOccurrences(string, substring): 
    count = 0
    start = 0
  
    while start < len(string): 
        pos = string.find(substring, start) 
 
        if pos != -1: 
            start = pos + 1
            count += 1
        else: 
            break
    return count 

N,Q = list(map(int,input().split()))
S = input()
for _ in range(Q):
        data = list(input().split())
        if data[0] == '1':
                print(CountOccurrences(S,data[1]))
        else:
                L = int(data[1])
                R = int(data[2])
                W = data[3]
                temp = list(S)
                c = 0
                for i in range(L-1,R):
                        temp[i] = W[c]
                        c += 1
                S = ''.join(temp)