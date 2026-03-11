class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        self.p = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.p[i][j] = matrix[i-1][j-1] + self.p[i-1][j] + self.p[i][j-1] - self.p[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.p[row2+1][col2+1] - self.p[row1][col2+1] - self.p[row2+1][col1] + self.p[row1][col1]
