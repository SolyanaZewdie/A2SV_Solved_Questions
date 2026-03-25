import math
class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        prev = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                k = (nums[i] + prev - 1) // prev  
                operations += k - 1
                prev = nums[i] // k

        return operations