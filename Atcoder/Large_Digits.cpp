/*
        Problem Statement : A - Large Digits
        Link : https://atcoder.jp/contests/abc187/tasks/abc187_a
        Score : accepted
*/

#include<iostream>
using namespace std;

int check_sum(int number)
{
        int sum=0;
        while(number)
        {
                int digit = number%10;
                sum = sum + digit;
                number = number/10;
        }
        return(sum);
}

int main()
{
        int A,B;
        cin>>A>>B;
        int sum_A = check_sum(A);
        int sum_B = check_sum(B);
        if (sum_A > sum_B)
        {
                cout<<sum_A;
        }
        else
                cout<<sum_B;
        
        return 0;
}