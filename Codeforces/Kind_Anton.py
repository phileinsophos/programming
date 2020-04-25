'''
Problem Statement : Kind Anton
Link : https://codeforces.com/problemset/problem/1333/B
score : partially accepted
'''

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if a[0]!=b[0]:
        print('NO')
    else:
        for index in range(n-1,0,-1):
            diff = abs(a[index] - b[index])
            new_value = abs(a[index] + a[index-1])
            while new_value <= diff:
                a[index] = a[index] + a[index-1]
                if abs(a[index] + a[index-1]) != new_value:
                    new_value = abs(a[index] + a[index-1])
                else:
                    break
                if a==b:
                    break
                
                
                
        if a==b:
            print('YES')
        else:
            print('NO')

