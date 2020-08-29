/*
 
    Problem Statement : Two Strings
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/submissions/
    Score : accepted
 
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        string st1,st2;
        cin>>st1>>st2;

        int counts = 0;
        for(int i=0;i<st1.length();i++)
        {   
            bool found_char = false;
            for(int j=0;j<st1.length();j++)
            {
                if(st1[i] == st2[j])
                {
                    st2.replace(j,1,"_");
                    counts++;
                    found_char = true;
                    break;
                }
            }
            if(!found_char)
                break;
        }
        if(counts==st1.length())
            cout<<"YES\n";
        else
        {
            cout<<"NO\n";
        }
        
    }    
    return 0;
}