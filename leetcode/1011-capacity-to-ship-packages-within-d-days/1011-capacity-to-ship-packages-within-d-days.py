class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(capacity):
            days_needed = 1
            current_load = 0
        
            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += w
        
            return days_needed <= days

        left = max(weights)
        right = sum(weights)
    
        while left < right:
            mid = (left + right) // 2
        
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
    
        return left   