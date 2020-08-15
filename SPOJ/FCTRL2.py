'''

 	 Problem Statement : Small factorials
 	 Link : https://www.spoj.com/problems/FCTRL2/
 	 Score : accepted

 '''
def fact(number):
    factorial = 1
    for i in range(number,1,-1):
        factorial *= i
    return factorial

for _ in range(int(input())):
    n = int(input())
    print(fact_rec(n))
