'''
    Problem Statement : Beautiful Matrix
    Link : https://codeforces.com/problemset/problem/263/A
    score : accepted
'''
r_num = 1
c_num = None
moves = None
for _ in range(5):
    row = list(map(int,input().split()))
    if 1 in row:
        c_num = row.index(1)+1
        moves = abs(r_num-3)+abs(c_num-3)
        
    r_num += 1
print(moves)

