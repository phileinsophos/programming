/*

 	 Problem Statement : What’s Next
 	 Link : https://www.spoj.com/problems/ACPC10A/
 	 Score : accepted

 */

#include<iostream>
using namespace std;

int main()
{
  while(true)
  {
    int n1,n2,n3;
    cin>>n1>>n2>>n3;
    if(n1==0 && n2==0 && n3==0)
    {
      break;
    }
    else
    {
      if(n2-n1 == n3-n2)
      {
        cout<<"AP "<<n3+(n2-n1)<<'\n';
      }
      else
      {
        cout<<"GP "<<n3*int(n2/n1)<<'\n';
      }

    }
  }

  return 0;
}
