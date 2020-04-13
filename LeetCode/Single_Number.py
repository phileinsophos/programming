'''
Problem Statement : Single Number
Link : https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
score : accepted
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i

