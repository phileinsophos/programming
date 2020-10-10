/*
    Problem Statement : Chef and Easy Queries
    Link : https://www.codechef.com/OCT20B/problems/CHEFEZQ
    Score : partially accepted - 20 pts
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll test;
    cin>>test;
    while(test--)
    {
        ll n,k,free_day=0,carry=0;
        cin>>n>>k;
        ll queries;
        for(ll i=0;i<n;i++)
        {
            cin>>queries;
            carry += queries;
            if(carry >= k )
            {
                carry -= k;
            }
            else
            {
                if(free_day==0)
                    free_day = i+1;
            }
        } 
        if(free_day==0)
        {
            free_day = n;
            while(carry >= k)
            {
                carry -= k;
                free_day++;
            }
            free_day++;
        }
        cout<<free_day<<"\n";
    }

    return 0;
}