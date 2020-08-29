/*
 
    Problem Statement : Split houses
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/split-house-547be0e9/submissions/
    Score : accepted
 
*/

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<math.h>
using namespace std;


int main()
{
    int N;
    cin>>N;
    string houses;
    bool possible= true;
    int fences =0; 
    cin>> houses;
    for(int i=0;i<N;i++)
    {
        if(houses[i]=='.')
        {
            houses[i]='B';
            fences++;
        }
        else if(houses[i+1]=='H')
        {   
                possible = false;
                break;
        }  
    }
    if(possible)
    {
        cout<<"YES\n"<<houses;

    }
    else
        cout<<"NO\n";

    return 0;
}