'''
    Problem Statement : Odd divisors 
    Link : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/odd-divisors-1-4939f17d/description/
    Score : 7 - memory limit exceeding for large inputs 
'''
test = int(input())
for t in range(test):
    N,M = list(map(int,input().split()))
    total = [1 for i in range(N)]
    for divisor in range(3,N+1,2):
        for index in range(divisor,N+1,divisor):
            if index%divisor==0:
                total[index-1] = divisor
    print(sum(total)%M)
            

