'''
    Problem Statement : Maximum Product of Two Elements in an Array
    Link : https://leetcode.com/contest/weekly-contest-191/problems/maximum-product-of-two-elements-in-an-array/
    Score : accepted
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answers = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a = (nums[i]-1)*(nums[j]-1)
                answers.append(a)
        return max(answers)
        