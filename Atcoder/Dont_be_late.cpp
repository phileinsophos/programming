/*
 
    Problem Statement : Don't be late
    Link : https://atcoder.jp/contests/abc177/tasks/abc177_a
    Score : accepted
 
*/

#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    long D,T,S;
    cin>>D>>T>>S;
    if((T*S)>=D)
        cout<<"YES\n";
    else
        cout<<"NO\n";
    return 0;
}