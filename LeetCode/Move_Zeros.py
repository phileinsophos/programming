'''
Problem Statement : Move Zeros
Link : https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
score : accepted
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        length = len(nums)
        zeros = 0
        while index<length:
            if nums[index] == 0:
                zeros +=1 
                nums.pop(index)
                length -= 1
            else:
                index += 1
        for i in range(zeros):
            nums.insert(len(nums),0)

