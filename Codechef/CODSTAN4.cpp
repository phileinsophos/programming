/*
    Problem Statement : Equal Chocolates 
    Link : https://www.codechef.com/CFUN2020/problems/CODSTAN4
    Score : accepted
*/

#include<iostream>
using namespace std;

int main()
{
    int M,R;
    cin>>M>>R;
    if(R%M==0)
        cout<<"Yes";
    else
    {
        cout<<"No";
    }
    
    return 0;
}