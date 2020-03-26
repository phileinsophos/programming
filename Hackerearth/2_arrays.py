'''
    Problem Statement : 2 Arrays
    Link : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/2-arrays-90c9019c/description/
    score = 8.8
'''

N = input()
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))

A_contain = -1 in A
B_contain = -1 in B

num_A_contain = A.count(-1)
num_B_contain = B.count(-1)

sumA = sum(A)
sumB = sum(B)

count_ways=0
if(sumA==sumB):
    print("Infinite")
elif (A_contain==True and B_contain=False):
    index = A.index(-1)
else:
    print("Infinite")
