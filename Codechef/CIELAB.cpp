/*
 
    Problem Statement : Ciel and A-B Problem
    Link : https://www.codechef.com/problems/CIELAB
    Score : accepted
 
*/
#include<iostream>
using namespace std;

struct Node
{
    int digit;
    Node *next;
};

struct Node *head;

void insert_node(int num)
{
    if(head==NULL)
    {
        head = new Node;
        head->digit = num;
        head->next = NULL;
    }
    else
    {
        struct Node *p = new Node;
        p->digit = num;
        p->next = head;
        head = p;
    }
}

void create_list(int number)
{
    while(number!=0)
    {
        int dig = number%10;
        insert_node(dig);
        number = number/10;
    }
}

void display_list()
{
    struct Node *temp = head;
    while(temp!=NULL)
    {
        cout<<temp->digit;
        temp = temp->next;
    }
}

void generate_answer()
{
    struct Node *temp = head;
    while(temp->next!=NULL)
        temp=temp->next;
    if(temp->digit == 9)
        temp->digit--;
    else
        temp->digit++;
}
int main()
{
    head=NULL;
    int a,b;
    cin>>a;
    cin>>b;
    create_list(a-b);
    generate_answer();
    display_list();
    return 0;
}