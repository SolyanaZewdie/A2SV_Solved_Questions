class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        
        def backtrack(curr):
            if len(res) >= k:
                return
            
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        
        backtrack("")
        
        return res[k-1] if k <= len(res) else ""