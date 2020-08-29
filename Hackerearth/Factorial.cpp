/*

 	 Problem Statement : Factorial
 	 Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/submissions/
 	 Score : accepted

 */
#include<iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;
  int fact = 1;
  for(int i=n;i>1;i--)
  {
    fact = fact * i;
  }
  cout<<fact<<'\n';

  return 0;
}
