'''
  Problem Statement : Sum square difference
  Link : https://projecteuler.net/problem=6
  Score : accepted
'''

import math;
x=0
y=0
for i in range(1,101):
  x=x+pow(i,2);
for j in range(1,101):
  y=y+j;
y=pow(y,2);  

print("\n\n",x,"\n",y,"\n\n",(y-x));
    
