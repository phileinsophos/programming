'''
    Problem Statement : GCD Choice
    Link : https://www.hackerearth.com/challenges/competitive/october-easy-20/algorithm/gcd-choice-f04433f3/
    Score : partially accepted - 43 pts
'''

def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

n = int(input())
numbers = list(map(int,input().split()))

if(n>2):
    minimum = min(numbers)  
    n -= 1
    numbers.remove(minimum)

gcd=find_gcd(numbers[0],numbers[1]) 

for i in range(2,n): 
    gcd=find_gcd(gcd,numbers[i]) 
      
print(gcd) 
