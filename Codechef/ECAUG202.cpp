/*
 
    Problem Statement : Angry Delta
    Link : https://www.codechef.com/ENAU2020/problems/ECAUG202
    Score : accepted
 
*/
#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int N,total=0;
        cin>>N;
        for(int i=0;i<N;i++)
        {
            int p;
            cin>>p;
            if(p%2==0)
                total += p;
        }
        cout<<total<<"\n";
        
    }
    return 0;
}