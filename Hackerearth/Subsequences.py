'''
Problem Statement : Subsequences
Link : https://www.hackerearth.com/challenges/competitive/april-easy-20/algorithm/subsequence-again-19245c50/
score : 30pts - partially accepted
'''

from itertools import combinations
def check_sum_subsequences(number):
    total = 0
    for p_len in range(1,len(number)+1):
        per = combinations(number,r=p_len)
        for p in per:
            sub = int(''.join(p))
            total += sub
    if total%2==0:
        return False
    else:
        return True
    
    
Q = int(input())
for _ in range(Q):
    K = int(input())
    L = 1
    R = 1
    while K:
        if check_sum_subsequences(str(R)):
            K -= 1
        R += 1
    print(L,R-1)

