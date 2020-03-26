/*
    Problem Statement : Tree query - Segment Trees - Hackerearth
    Link : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/tree-query-3-5d98588f/description/
    score : 0.5
*/


#include<iostream>
using namespace std;

int main()
{
    int n,q;
    cin >> n >> q;
    int matrix[n][n], status[n];
    for(int i =0;i<n;i++)
    {
        status[i] = 1;
    }
    for(int i =0;i<n;i++)
    {
        for(int j =0;j<n;j++)
        {
            matrix[i][j] = 0;
        }
    }
    for(int i =0;i<n-1;i++)
    {
        int x,y;
        cin >> x >> y;
        matrix[x-1][y-1] = matrix[y-1][x-1] = 1;
    }
    for(int i =0;i<q;i++)
    {
        int x,y;
        cin >> x >> y;
        y--;
        if(x == 1)
        {
            if(status[y] == 0)
            {
                status[y] = 1;
            }
            else
            {
                status[y] = 0;
            }
        }
        else
        {
            int count = 0;
            for(int i = 0; i<n;i++)
            {
                if (matrix[y][i] == 1 && status[i] == 1 && status[y] == 1)
                {
                    count++;
                }
            }
            cout << "--- "<<count << '\n';
        }

        cout<<"\n Two Dimensional Array is : \n";
        for(int i=0; i<n; i++)
        {
                for(int j=0; j<n; j++)
                {
                        cout<<" "<<matrix[i][j]<<" ";
                }
                cout<<"\n";
        }
        cout << "status --- ";
        for(int j=0; j<n; j++)
                {
                        cout<<" "<<status[j]<<" ";
                }
        cout << "\n\n";
    }
    return 0;
}