/*
 
    Problem Statement : Substring
    Link : https://atcoder.jp/contests/abc177/tasks/abc177_b
    Score : accepted
 
*/

#include<iostream>
#include<limits.h>
using namespace std;

int main()
{
    string s1,s2;
    cin>>s1;
    cin>>s2;
    int count = INT_MAX;
    int j=0,i=0;
    int diff = s1.length()-s2.length();
    while(diff>=0)
    {
        int temp_i=i;
        int temp_count = 0;
        while(j<s2.length())
        {
            if(s1[temp_i]!=s2[j])
            {
                temp_count++;
            }
            temp_i++;
            j++;
        }
        if(temp_count<count)
        {
            count = temp_count;
        }
        diff--;
        i++;
        j=0;
    }
    cout<<count<<"\n";
}