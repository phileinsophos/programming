/*
	 Problem Statement : Small Factorial
	 Link : https://www.codechef.com/problems/FLOW018
	 Score : accepted
*/

#include <iostream>
using namespace std;

int factorial(int number)
{
    int factor = 1;
    for(int i=number;i>1;i--)
        factor = factor*i;
    return(factor);
}

int main() {
	int test;
	cin>>test;
	for(int i=0;i<test;i++)
	{
	    int number;
	    cin >> number;
	    cout<<factorial(number)<<'\n';
	    
	}
	return 0;
}
