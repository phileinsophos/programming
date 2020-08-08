'''

 	 Problem Statement : Special numbers
 	 Link : https://www.hackerearth.com/challenges/competitive/august-easy-201/algorithm/happy-numbers-4a67748e/
 	 Score : 32 - partially accepted

 '''

from itertools import permutations, combinations

def check_coprime(numbers):
    left, right = numbers
    smallest = left
    if right < left:
        smallest = right

    if left%smallest==0 and right%smallest==0:
            return False

    if left%2==0 and right%2==0:
            return False
    else:
        for i in range(3,smallest+1,2):
            if left%i==0 and right%i==0:
                return False
    return True

N  = int(input())
special_numbers = []
for i in range(4,N+1):
    if str(i).count('4')+str(i).count('7') == len(str(i)):
        special_numbers.append(i)

p = combinations(special_numbers,2)
pairs = 0
for t in p:
    pairs += check_coprime(t)

print(pairs)
