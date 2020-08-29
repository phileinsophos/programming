/*
 
    Problem Statement : Duration
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/duration/submissions/
    Score : accepted
 
*/
#include<iostream>
using namespace std;

int main()
{
    int N;
    cin>> N;
    while(N--)
    {
        int SH,SM,EH,EM;
        cin>>SH>>SM>>EH>>EM;
        int minutes=0,hours=0;
        while(SM!=EM)
        {
            minutes++;
            SM++;
            if(SM==60)
            {
                SM=SM%60;
                SH++;
            }
        }
        while(SH!=EH)
        {
            hours++;
            SH++;
        }
        cout<<hours<<" "<<minutes<<'\n';
    }
    return 0;
}