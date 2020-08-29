
/*

 	 Problem Statement : Cost of balloons
 	 Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/submissions/
 	 Score : accepted

 */
#include<iostream>
using namespace std;

int main()
{
  int test;
  cin>>test;
  while(test--)
  {
    int b1,b2;
    cin>>b1>>b2;
    int N;
    cin>>N;
    int problem1[N],problem2[N];
    int p1=0,p2=0;
    for(int i=0;i<N;i++)
    {
      cin>>problem1[i]>>problem2[i];
      if(problem1[i]==1)
        p1++;
      if(problem2[i]==1)
        p2++;
    }
    int cost1 = p1*b1+p2*b2;
    int cost2 = p1*b2+p2*b1;
    if(cost1 > cost2)
      cout<<cost2<<'\n';
    else
      cout<<cost1<<'\n';

  }
  return 0;
}
