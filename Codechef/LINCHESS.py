'''

 	 Problem Statement : Chef and Linear Chess
 	 Link : https://www.codechef.com/AUG20B/problems/LINCHESS
 	 Score : accepted

 '''
for _ in range(int(input())):
    N, K = list(map(int,input().split()))
    P = list(map(int,input().split()))
    max_value = max(P)+1
    moves = []
    for i in P:
        if K%i==0:
            moves.append(K//i)
        else:
            moves.append(max_value)
    min_moves = min(moves)
    player_index = moves.index(min_moves)
    if moves[player_index] != max_value:
        print(P[player_index])
    else:
        print(-1)
