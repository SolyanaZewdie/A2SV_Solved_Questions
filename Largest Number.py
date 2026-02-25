class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if compare(nums[i], nums[j]) > 0:
                    nums[i], nums[j] = nums[j], nums[i]
        
        result = ''.join(nums)
        
        return '0' if result[0] == '0' else result
