class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        result = []
        total = rows * cols
        
        r, c = rStart, cStart
        result.append([r, c])
        
        steps = 1
        
        while len(result) < total:
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            steps += 1
            
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            steps += 1
        
        return result
