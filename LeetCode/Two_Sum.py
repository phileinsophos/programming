'''
    Problem Statement : Two Sum
    Link : https://leetcode.com/problems/two-sum/
    Score : accepted
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in nums:
            temp_list = nums.copy()
            index = nums.index(number)
            remainder = target - number
            temp_list[index] = 'a'
            if remainder in temp_list:
                return([nums.index(number),temp_list.index(remainder)])

