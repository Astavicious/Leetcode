class Solution(object):
    def twoSum(self, nums, target):
        left=0
        right=len(nums)-1
        x=nums[:]
        l2=[]
        nums.sort()
        while left<right:
            if target>nums[left]+nums[right]:
                left+=1;
            elif target<nums[left]+nums[right]:
                right-=1;
            else:
                l1=[]
                l1.append(nums[left])
                l1.append(nums[right])
                break;
        for i in range(len(x)):
            if x[i]==l1[0]:
                l2.append(i)
                continue
            if x[i]==l1[1]:
                l2.append(i)
            if len(l2)==2:
                break
        return l2                



        
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        