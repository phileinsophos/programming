/*
 
    Problem Statement : Chef and Missing Numbers
    Link : https://www.codechef.com/BING2020/problems/CHEF1002
    Score : accepted
 
*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
        int N;
        cin>>N;
        vector <int> original;
        for(int i=0;i<N;i++)
        {
            int p;
            cin>>p;
            original.push_back(p);
        }
        int M;
        cin>>M;
        vector <int> partial;
        for(int i=0;i<M;i++)
        {
            int p;
            cin>>p;
            partial.push_back(p);
        }
        vector <int> lost_numbers;
        
        for(int i=0;i<M;i++)
        {
            if(count(original.begin(),original.end(),partial[i]))
            {
                auto it = find(original.begin(),original.end(),partial[i]);
                original.erase(it);
            }
            else
            {   
                lost_numbers.push_back(partial[i]);
            }
            
        }
        sort(lost_numbers.begin(),lost_numbers.end());
        for(int i=0;i<lost_numbers.size();i++)
            cout<<lost_numbers[i]<<" ";
        cout<<"\n";
        
        return 0;
}