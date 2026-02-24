class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        
        for i in range(n):
            left = 0
            right = n - 1
            while left <= right:
                image[i][left], image[i][right] = image[i][right] ^ 1, image[i][left] ^ 1
                left += 1
                right -= 1
        
        return image
