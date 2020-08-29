/*

 	 Problem Statement : Mutated Minions
 	 Link : https://www.codechef.com/problems/CHN15A
 	 Score : accepted

 */
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--) {
	    int n,k,mutations = 0;
	    cin>>n>>k;
	    for(int i=0;i<n;i++)
      {
          int t;
	        cin>>t;
          t = t+k;
          if(t%7==0)
            mutations++;
	    }
      cout<<mutations<<'\n';
	}

	return 0;
}
