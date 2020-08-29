/*

 	 Problem Statement : Toggle String
 	 Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/submissions/
 	 Score : accepted

 */
#include<iostream>
#include <string.h>
#include <ctype.h>
using namespace std;

int main()
{
  string st;
  cin>>st;
  for(int i=0;i<st.length();i++)
  {
    if(isupper(st[i]))
    {
      st[i] = tolower(st[i]);
    }
    else
      st[i] = toupper(st[i]);
  }
  cout<<st<<'\n';
  return 0;
}
