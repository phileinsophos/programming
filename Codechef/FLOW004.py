'''
Problem Statement : First and Last Digit
Link : https://www.codechef.com/problems/FLOW004
score : accepted
'''

for _ in range(int(input())):
    number = list(map(int,input()))
    print(number[0] + number[-1])

