'''
Problem Statement : Enormous Input Test 
Link : https://www.codechef.com/problems/INTEST
score : accepted
'''
n,k = list(map(int,input().split()))
count = 0
for _ in range(n):
    num = int(input())
    if num%k ==0:
        count += 1
        
print(count)

