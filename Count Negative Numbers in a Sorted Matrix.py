class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        row = m - 1
        col = 0
        count = 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)
                row -= 1
            else:
                col += 1
        
        return count
