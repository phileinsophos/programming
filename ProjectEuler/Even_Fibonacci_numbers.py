'''
Problem Statement : Even Fibonacci numbers
Link : https://projecteuler.net/problem=2
score : accepted
'''

n1 = 0
n2 = 1
term = 1
next_term = n1+n2
even_sum = 0
while next_term < 4000000:
    next_term = n1+n2
    if next_term%2==0:
        even_sum += next_term
    n1 = n2
    n2 = next_term
    term += 1
print(even_sum)

