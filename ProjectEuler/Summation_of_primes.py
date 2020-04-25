'''
Problem Statement : Summation of primes
Link : https://projecteuler.net/problem=10
score : accepted
'''

N = 2000000
is_prime = [True for i in range(N+1)]
p = 2
while (p*p < N):
    if is_prime[p] == True:
        for i in range(p*p,N+1,p):
            is_prime[i] = False
    p += 1
is_prime[0] = False
is_prime[1] = False
sum_of_primes = 0
for i in range(N+1):
    if is_prime[i]:
        sum_of_primes += i
print(sum_of_primes)

