/*
 
    Problem Statement : Chef and Loss
    Link : https://www.codechef.com/BING2020/problems/CHEF1003
    Score : accepted
 
*/

#include<iostream>
#include<vector>
#include<algorithm>
#include<stdlib.h>
using namespace std;

int main()
{
    long long N;
    cin>>N;
    long long prices[N];
    for(long long i=0;i<N;i++)
        cin>>prices[i];
    vector <long long> final_loss;
    for(long long i=0;i<N-1;i++)
    {
        vector <long long> current_loss;
        for(long long j=i+1;j<N;j++)
        {
            long long p = prices[i] - prices[j];
            if(p>0)
            {
                current_loss.push_back(abs(p));
            }
        }
        if(current_loss.size()>0)
            final_loss.push_back(*min_element(current_loss.begin(),current_loss.end()));
    }
    cout<<*min_element(final_loss.begin(),final_loss.end());
    return 0;
}