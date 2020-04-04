'''
Problem Statement : Next Round
Link : https://codeforces.com/problemset/problem/158/A
score : accepted
'''

N,K = list(map(int,input().split()))
scores = list(map(int,input().split()))
thershold = scores[K-1]
index = 0
for i,j in enumerate(scores):
    if j == thershold:
        index = i
        
count = 0
for i in range(index+1):
    if scores[i] > 0 and scores[i] >= thershold:
        count += 1
print(count)

