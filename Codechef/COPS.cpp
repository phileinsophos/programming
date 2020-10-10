
/*

 	 Problem Statement : Cops and the Thief Devu
 	 Link : https://www.codechef.com/problems/COPS
 	 Score : accepted

 */
#include <iostream>
#include<bits/stdc++.h>
#include<string.h>
#include<vector>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--)
  {
	    int M,Y,X;
      cin>>M>>X>>Y;
      int houses[100];
      for(int i=0;i<100;i++)
        houses[i] = 1;

      int cop_range = X*Y;
      int cop_house[M];
      for(int i=0;i<M;i++)
      {
        cin>>cop_house[i];
      }
      for(int i=0;i<M;i++)
      {
        int start=0,end=100;
        if((cop_house[i] - cop_range) > 0)
          start = (cop_house[i] - cop_range)-1;
        if((cop_house[i] + cop_range) < 100)
          end = (cop_house[i] + cop_range)-1;

        for(int j=start;j<=end;j++)
          houses[j] = 0;

      }
      int remaining_houses = 0;
      for(int i=0;i<100;i++)
      {
        if(houses[i]==1)
          remaining_houses++;
      }
      cout<<remaining_houses<<'\n';
  }
  return 0;
}
