import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """


        heaters.sort()
        radius = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            
            left_dist = float('inf') if i == 0 else house - heaters[i - 1]
            
            right_dist = float('inf') if i == len(heaters) else heaters[i] - house
            
            closest = min(left_dist, right_dist)
            
            radius = max(radius, closest)
        
        return radius       