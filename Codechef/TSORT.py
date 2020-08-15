'''
Problem Statement : Turbo Sort
Link : https://www.codechef.com/problems/TSORT
score : accepted
'''

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
numbers.sort()
print(*numbers,sep='\n')