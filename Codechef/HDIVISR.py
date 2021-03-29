'''
    Problem Statement : Highest Divisor 
    Link : https://www.codechef.com/problems/HDIVISR
    Score : accepted
'''

N = int(input())
divisor = 0
for i in range(10,0,-1):
    if N%i ==0:
        divisor = i
        break
print(divisor)