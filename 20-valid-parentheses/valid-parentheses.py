class Solution(object):
    def isValid(self, s):
        lifo=[]
        for i in range(len(s)):
            if(s[i]=='[' or s[i]=='{' or s[i]=='('):
                lifo.append(s[i])
            elif(s[i]==')' and  lifo and lifo[-1]=='('):lifo.pop()
            elif(s[i]=='}' and lifo and lifo[-1]=='{'):lifo.pop()
            elif(s[i]==']' and  lifo and lifo[-1]=='['):lifo.pop()
            else:
                return False
        isEmpty= not bool(lifo)
        return isEmpty



        