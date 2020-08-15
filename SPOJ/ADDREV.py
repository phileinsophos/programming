'''

 	 Problem Statement : Adding Reversed Numbers
 	 Link : https://www.spoj.com/problems/ADDREV/
 	 Score : accepted

 '''
for _ in range(int(input())):
    number1,number2 = input().split()
    number1 = int(number1[::-1])
    number2 = int(number2[::-1])
    number1 += number2
    number1 = int(str(number1)[::-1])
    print(number1)
