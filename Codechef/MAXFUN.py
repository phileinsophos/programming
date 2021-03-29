'''
    Problem Statement : Maximise Function
    Link : https://www.codechef.com/problems/MAXFUN
    Score : accepted
'''

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    x = numbers.pop(0)
    y = numbers.pop(-1)
    z = numbers.pop(0)
    
    answer = abs(x - y) + abs(y-z) + abs(z-x)
    print(answer)