'''
 
    Problem Statement : A Problem on Sticks
    Link : https://www.codechef.com/SEPT20B/problems/TREE2
    Score : accepted
 
'''

for _ in range(int(input())):
    N = int(input())
    sticks = set(map(int,input().split()))
    count = len(sticks)
    if 0 in sticks:
        count -= 1

    print(count)