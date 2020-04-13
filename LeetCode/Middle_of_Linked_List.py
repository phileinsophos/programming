'''
Problem Statement : Middle of the Linked List
Link : https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
score : accepted
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
                temp = head
                nodes = 0
                while temp.next!=None:
                    nodes += 1
                    temp = temp.next
                nodes += 1
                temp_nodes = nodes
                if nodes%2==0:
                    temp_nodes = math.ceil(nodes/2)
                else:
                    temp_nodes = math.ceil(nodes/2)-1
                temp = head
                
                while temp_nodes:
                    temp = temp.next
                    temp_nodes -= 1
                return temp
        

