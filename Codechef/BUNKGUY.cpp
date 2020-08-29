/*
 
	Problem Statement : THE BUNKING GUY
	Link : https://www.codechef.com/CEFT2020/problems/BUNKGUY
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
		int N;
		cin>>N;
		int students[N] = {};
		for(int i=0;i<N-1;i++)
		{
			int s;
			cin>>s;
			students[s-1] = 1;
		}
		for(int i=0;i<N;i++)
		{
			if(students[i]==0)
				cout<<i+1<<"\n";
		}

	}
	return 0;
}