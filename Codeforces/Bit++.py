'''
    Problem Statement : Bit++
    Link : https://codeforces.com/problemset/problem/282/A
    score : accepted
'''
X = 0
for _ in range(int(input())):
    s = input()
    if '+' in s:
        X += 1
    else:
        X -= 1
print(X)

