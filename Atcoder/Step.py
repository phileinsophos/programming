'''

 	 Problem Statement : Step
 	 Link : https://atcoder.jp/contests/abc176/tasks/abc176_c
 	 Score : accepted

 '''

N = int(input())
persons = list(map(int,input().split()))
stool_height = 0
for i in range(1,N):
    if persons[i] < persons[i-1]:
        height_req = abs(persons[i] - persons[i-1])
        persons[i] = persons[i]+height_req
        stool_height += height_req
print(stool_height)
