/*
 
    Problem Statement : Lift queries
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/lift-queries/submissions/
    Score : accepted
 
*/
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int test;
    cin>>test;
    int A=0,B=7;
    while(test--)
    {
        int lift_call;
        cin>>lift_call;
        if(abs(A-lift_call) < abs(B-lift_call))
        {
            cout<<"A\n";
            A = lift_call;
        }
        else if(abs(A-lift_call) > abs(B-lift_call))
        {
            cout<<"B\n";
            B = lift_call;
        }
        else
        {
            if(A < lift_call)
            {
                cout<<"A\n";
                A = lift_call;
            }
            else
            {
                cout<<"B\n";
                B = lift_call;
            }
            
        }
    }
    return 0;
}
