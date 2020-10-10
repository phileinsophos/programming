/*
    Problem Statement : Copying code
    Link : https://www.hackerearth.com/challenges/competitive/october-easy-20/algorithm/copying-code-3-b70a931b/
    Score : accepted
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long int

ll method1(ll lines, ll move_line)
{
    ll keys = 2;
    keys = keys + (lines - move_line);
    keys += 2;
    return(keys);
}

ll method2(ll lines, ll move_line)
{
    ll keys = 2;
    keys = keys * (lines - move_line);
    return(keys);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n,i;
    cin>>n>>i;
    ll m1 = method1(n,i);
    ll m2 = method2(n,i);
    if(m1 > m2 )
    {
        cout<<m2;
    }
    else
    {
        cout<<m1;
    }
    
    return 0;
}