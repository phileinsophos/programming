'''
    Problem Statement : 1389. Create Target Array in the Given Order
    Link : https://leetcode.com/contest/weekly-contest-181/problems/create-target-array-in-the-given-order/
    score : accepted
'''
class Solution:
    def createTargetArray(self,nums, index):
        '''
            runtime : 32ms
        '''
        final = []
        for number,ind in zip(nums,index):
            final.insert(ind,number)
        return final
    
    
    def createTargetArray2(self,nums, index):
        '''
            runtime : 20ms
        '''
        final = []
        for i in range(len(nums)):
            final.insert(index[i],nums[i])
        return final
    
nums = [1,2,3,4,0]
index = [0,1,2,3,0]

s = Solution()
#s.createTargetArray(nums,index)
s.createTargetArray2(nums,index)

