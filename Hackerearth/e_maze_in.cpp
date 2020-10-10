/*
 
    Problem Statement : e-maze-in
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/submissions/
    Score : accepted
 
*/

#include<iostream>
#include<string>
using namespace std;

int main()
{
    string st;
    cin>>st;
    int pos[] = {0,0};
    for(int i=0;i<st.length();i++)
    {
        switch(st[i])
        {
            case 'L':   pos[0] -= 1;
                        break;
            case 'R':   pos[0] += 1;
                        break;
            case 'U':   pos[1] += 1;
                        break;
            case 'D':   pos[1] -= 1;
                        break;
        }
    }
    cout<<pos[0]<<" "<<pos[1];
    return 0;
}