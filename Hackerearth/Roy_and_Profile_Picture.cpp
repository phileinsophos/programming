/*

 	 Problem Statement : Roy and Profile Picture
 	 Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/submissions/
 	 Score : accepted

 */
#include<iostream>
using namespace std;

int main()
{
  int L;
  cin>>L;
  int N;
  cin>>N;
  for(int i=0;i<N;i++)
  {
    int w,h;
    cin>>w>>h;
    if(w < L || h < L)
    {
      cout<<"UPLOAD ANOTHER\n";
    }
    else
    {
      if(w==h)
        cout<<"ACCEPTED\n";
      else
        cout<<"CROP IT\n";
    }
  }
  return 0;
}
