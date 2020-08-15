'''
Problem Statement : The Lead Game
Link : https://www.codechef.com/problems/TLG
score : accepted
'''

N = int(input())

winner = 0
lead = 0
player1 = 0
player2 = 0
for _ in range(N):
    a,b = list(map(int,input().split()))
    player1 += a
    player2 += b
    if abs(player1-player2) > lead:
        lead = abs(player2-player1)
        if player1 > player2:
            winner = 1
        else:
            winner = 2
print(winner,lead)    

