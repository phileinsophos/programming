/*

 	 Problem Statement : Chef Wars - Return of the Jedi
 	 Link : https://www.codechef.com/AUG20B/problems/CHEFWARS
 	 Score : accepted

 */

#include<iostream>
#include<math.h>
using namespace std;

int main()
{
	int test;
	cin >> test;
	for(int i=0;i<test;i++)
	{
		int H,P;
		cin>>H>>P;
		bool win = true;
		while(H>0)
		{
			H = H-P;
			P = floor(P/2);
			cout<<"H-"<<H<<" P-"<<P<<'\n';
			if(P<=0 and H>0)
			{
				win = false;
				break;
			}
		}
		if(win)
			cout<<1<<'\n';
		else
			cout<<0<<'\n';
	}
	return 0;
}
