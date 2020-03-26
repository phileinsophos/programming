'''
    Problem Statement : XOR Ranges
    Link : https://www.hackerearth.com/problem/algorithm/xoring-ranges-1-4a2b7724/
    score : partially accepted
'''

from functools import reduce
from operator import xor

q = int(input())
data = list()
for i in range(q):
    inp = list(map(int,input().split(" ")))
    if inp[0]==1:
        data.insert(0,inp[1])
    if inp[0]==2:
        data.append(inp[1])
    if inp[0]==3:
        x = inp[1]
        y = inp[2]
        ans = reduce(xor,data[x-1:y])
        print(ans)
