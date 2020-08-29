/*

 	 Problem Statement : Chef and Notebooks
 	 Link : https://www.codechef.com/problems/CNOTE
 	 Score : accepted

 */

#include<iostream>
#include<vector>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	cin >>test;
	for(int i=0;i<test;i++)
	{
    int X,Y,K,N;
    cin>>X>>Y>>K>>N;
    int ith_book = -1, ith_pages=-1;
    int pages[N],cost[N];
    for(int j=0;j<N;j++)
    {
      cin>>pages[j]>>cost[j];
      if(cost[j] <= K && pages[j] >= ith_pages)
      {
        ith_book = j;
        ith_pages = pages[j];
      }
    }
    if(ith_book != -1)
    {
      int required_pages = X-Y;
      if(pages[ith_book] >= required_pages)
        cout<<"LuckyChef\n";
      else
        cout<<"UnluckyChef\n";
    }
    else
      cout<<"UnluckyChef\n";
  }
}
