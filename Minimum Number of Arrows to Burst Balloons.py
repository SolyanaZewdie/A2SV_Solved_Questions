class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        points.sort()
        
        arrows = 0
        i = 0
        n = len(points)
        
        while i < n:
            arrows += 1
            end = points[i][1]
            i += 1
            
            while i < n and points[i][0] <= end:
                if points[i][1] < end:
                    end = points[i][1]
                i += 1
        
        return arrows
