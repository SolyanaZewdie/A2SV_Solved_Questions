class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                
                a = num[:i]
                b = num[i:j]
                
                if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                    continue
                
                if self.isValid(a, b, num[j:]):
                    return True
        
        return False
    
    def isValid(self, a, b, remaining):
        while remaining:
            c = str(int(a) + int(b))
            
            if not remaining.startswith(c):
                return False
            
            remaining = remaining[len(c):]
            a, b = b, c
        
        return True
