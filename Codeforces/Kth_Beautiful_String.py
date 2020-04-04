'''
    Problem Statement : K-th Beautiful String
    Link : https://codeforces.com/contest/1328/problem/B
    score : TLE
'''

from itertools import combinations as COMB
from itertools import permutations as PER

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    a = ['a']*(n-2)
    b = ['b']*2

    letters = a + b


    q = PER(letters,n)
    strings = []
    for i in q:
        last = None
        generated = ''.join(i)
        if strings:
            last = strings[-1]
            if generated > last:
                strings.append(generated)
        else:
            strings.append(generated)
    print(strings[k-1])