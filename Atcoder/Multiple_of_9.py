'''

 	 Problem Statement : Multiple of 9
 	 Link : https://atcoder.jp/contests/abc176/tasks/abc176_b
 	 Score : accepted

 '''
number = list(map(int,list(input())))
if sum(number)%9==0:
    print("Yes")
else:
    print("No")
