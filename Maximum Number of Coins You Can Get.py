class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)
        result = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            right -= 1
            result += piles[right]
            right -= 1
            left += 1
        
        return result
