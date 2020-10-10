/*
 
    Problem Statement : Bricks Game
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/submissions/
    Score : accepted
 
*/

#include<iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    string final_brick = "None";
    int round = 1;
    while(N > 0)
    {   
        if(N - round <=0)
        {
            final_brick = "Patlu";
            break;
        }
        N -= round;

        if(N - (round*2) <= 0)
        {
            final_brick = "Motu";
            break;
        }
        N -= (round*2);

        round++; 
    }
    cout<<final_brick;
    return 0;
}