class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        cur=""
        k=0
        
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=='[':
                stack.append((cur,k))
                cur=""
                k=0
            elif c==']':
                prev,num=stack.pop()
                cur=prev+cur*num
            else:
                cur+=c
        
        return cur