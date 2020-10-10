/*
    Problem Statement : Covid Run
    Link : https://www.codechef.com/OCT20B/problems/CVDRUN
    Score : accepted
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int test;
    cin>>test;
    while(test--)
    {
        int N,K,X,Y;
        cin>>N>>K>>X>>Y;
        bool infected[N], my_city_safe = true;
        int total_cities = N;
        memset(infected,false,sizeof(infected)); 
        while(total_cities)
        {
            if(infected[Y-1]==true)
            {
                my_city_safe = false;
                break;
            }
            if(infected[X-1]==true)
            {
                break;
            }
            infected[X-1] = true;
            X = (X+K)%N;
            total_cities--;
        }
        
        if(my_city_safe)
        {
            cout<<"NO\n";
        }
        else
        {
            cout<<"YES\n";
        }
        
    }
    return 0;
}