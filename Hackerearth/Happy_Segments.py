'''
Problem Statement : Happy Segments
Link : https://www.hackerearth.com/challenges/competitive/april-circuits-20/algorithm/happy-segments-e290faa6/
score : 4pts - partially accepted - TLE
'''

n,m = list(map(int,input().split()))
a1 = list(map(int,input().split()))
b1 = list(map(int,input().split()))
q = int(input())
for _ in range(q):
    l,r = list(map(int,input().split()))
    happy = True
    done = []
    for element in set(a1[l-1:r]):
        if element not in done and a1[l-1:r].count(element) != b1[element-1]:
            happy = False
            break
    if happy:
        print(1)
    else:
        print(0)
        

