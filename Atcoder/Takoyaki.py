'''

 	 Problem Statement : Takoyaki
 	 Link : https://atcoder.jp/contests/abc176/tasks/abc176_a
 	 Score : accepted

 '''

N,X,T = list(map(int,input().split()))
total_munites = 0
while N>0:
    total_munites += T
    N -= X
print(total_munites)
