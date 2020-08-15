'''
Problem Statement : Counting Pretty Numbers
Link : https://www.codechef.com/problems/NUM239
score : accepted
'''
pretty_numbers = [2,3,9]
for _ in range(int(input())):
    L,R = list(map(int,input().split()))
    found = 0
    for num in range(L,R+1):
        if int(str(num)[-1]) in pretty_numbers:
            found += 1
    print(found)

