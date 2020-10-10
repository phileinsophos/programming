/*
    Problem Statement : AND choice
    Link : https://www.hackerearth.com/challenges/competitive/october-easy-20/algorithm/and-choice-0e5db566/
    Score : partially accepted - 80 pts
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n;
    cin>>n;
    ll array[n];
    for(ll i=0;i<n;i++)
        cin>>array[i];

    int size = sizeof(array)/sizeof(array[0]);
    sort(array,array+size);

    ll n1 = array[n-2] & array[n-1];
    ll n2 = array[n-3] & array[n-2];

    if(n1>=n2)
    {
        cout<<n1;
    }
    else
    {
        cout<<n2;
    }
    return 0;
}