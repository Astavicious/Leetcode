class Solution(object):
    def isPalindrome(self, x):
        ori=x
        y=0
        while(x>0):           
            y=y*10+x%10
            x=x//10
        if ori==y: return True
        return False
        """
        :type x: int
        :rtype: bool
        """
        