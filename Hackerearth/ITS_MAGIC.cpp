/*
 
    Problem Statement : IT’S MAGIC
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/its-magic/submissions/
    Score : accepted
 
*/
#include<iostream>
#include<climits>
using namespace std;

int main()
{
    long long N,total=0;
    cin>>N;
    long long numbers[N];
    for(long long i=0;i<N;i++)
    {
        cin>>numbers[i];
        total += numbers[i];
    }
    bool is_divisible = false;
    long long smallest_index=LONG_MAX;
    for(long long i=0;i<N;i++)
    {
        if((total-numbers[i])%7==0)
        {
            is_divisible = true;
            
            if(numbers[smallest_index] > numbers[i])
            {
                smallest_index = i;
            }
        }
    }
    if(!is_divisible)
        smallest_index = -1;
    cout<<smallest_index;
    return 0;
}