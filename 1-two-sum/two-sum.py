class Solution(object):
    def twoSum(self, nums, target):
        return next(([i,j]for i in range(len(nums)-1) for j in range (i+1,len(nums)) if nums[i]+nums[j]==target),None)
        
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        