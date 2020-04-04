'''
    Problem Statement : Divisibility Problem
    Link : https://codeforces.com/contest/1328/problem/A
    score : accepted
'''

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    if a%b==0:
        print(0)
    else:
        reminder = a % b
        steps = b - reminder
        print(steps)

