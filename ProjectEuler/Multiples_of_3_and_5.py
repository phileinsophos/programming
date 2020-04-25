'''
Problem Statement : Multiples of 3 and 5
Link : https://projecteuler.net/problem=1
score : accepted
'''
N = 1000
numbers = []
for i in range(1,N):
    if i%3==0 or i%5 ==0:
        numbers.append(i)
print(sum(numbers))

