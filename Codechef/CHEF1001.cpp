/*
 
    Problem Statement : Chef and Ice Cream
    Link : https://www.codechef.com/BING2020/problems/CHEF1001
    Score : accepted
 
*/

#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int money,n_flavours;
        cin>>money;
        cin>>n_flavours;
        vector <int> price;
        vector <int> valid_purchase;
        for(int i=0;i<n_flavours;i++)
        {
            int p;
            cin>>p;
            price.push_back(p);
            if(money%p == 0)
            {
                valid_purchase.push_back(p);
            }
        }
        sort(valid_purchase.begin(),valid_purchase.end(),greater<int>());
        int index1 = 0,index2= 1;
        auto it = find(price.begin(),price.end(),valid_purchase[0]);
        index1 = distance(price.begin(),it);
        price.erase(it);

        it = find(price.begin(),price.end(),valid_purchase[1]);
        index2 = index2 + distance(price.begin(),it);
        if(index1 < index2)
            cout<<index1<<" "<<index2<<"\n";
        else
            cout<<index2<<" "<<index1<<"\n";
    }
    return 0;
}