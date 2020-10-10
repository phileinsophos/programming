/*
    Problem Statement : FRIENDS PARTY 
    Link : https://www.codechef.com/CFUN2020/problems/CODSTAN1
    Score : accepted
*/

#include<iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    char str[N];
    int v=0,h=0;
    for(int i=0;i<N;i++)
    {
        cin>>str[i];
        if(str[i]=='V')
            v++;
        else
        {
            h++;
        }
    }
    if(v>h)
        cout<<"Virat";
    else
    {
        cout<<"Harshit";
    }
    
    return 0;
}