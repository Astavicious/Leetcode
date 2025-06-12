class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            for key,value in d.items():
                if nums[i]==value:
                    return [key,i]
            d[i]= target -nums[i]



        
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        