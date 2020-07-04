'''
  Problem Statement : Power digit sum
  Link : https://projecteuler.net/problem=16 
  Score : accepted
'''

a=pow(2,1000);
sum=0;
while(a!=0):
  b=a%10;
  sum=sum+b;
  a=a/10;
print(sum)

