class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):return False
        sim=sorted(s)
        tim=sorted(t)
        s=sim
        t=tim
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True
        