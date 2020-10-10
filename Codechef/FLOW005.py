'''
    Problem Statement : Smallest Numbers of Notes 
    Link : https://www.codechef.com/problems/FLOW005
    Score : accepted
'''

for _ in range(int(input())):
    notes = [100,50,10,5,2,1]
    N = int(input())
    min_notes = 0
    for i in notes:
        if N>=i:
            min_notes += int(N/i)
            N = N%i
        if N==0:
            break
    print(min_notes)