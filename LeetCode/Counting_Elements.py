'''
Problem Statement : Counting Elements
Link : https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
score : accepted
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        found = 0
        number_choosen = [False]*len(arr)
        for element in set(arr):
            if element+1 in arr:
                count_element = arr.count(element)
                count_elementplus = arr.count(element+1)
                if count_elementplus == count_element :
                    found = found + count_elementplus
                else:
                    found = found + count_element
        return found

