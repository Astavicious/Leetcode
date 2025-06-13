class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            d[target-nums[i]]=i



        
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        