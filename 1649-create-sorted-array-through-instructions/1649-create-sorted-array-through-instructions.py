class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        m = max(instructions)
        bit = [0] * (m + 1)
        
        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        total_cost = 0
        mod = 10**9 + 7
        
        for i, x in enumerate(instructions):
            count_less = query(x - 1)
            count_greater = i - query(x)
            
            cost = count_less if count_less < count_greater else count_greater
            total_cost += cost
            update(x)
            
        return total_cost % mod