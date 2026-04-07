class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        res = []
        stack = []
        
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
        
        return ''.join(res)       