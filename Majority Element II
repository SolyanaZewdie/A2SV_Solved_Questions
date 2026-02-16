class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        n = len(nums)
        
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        
        result = []
        for num in counts:
            if counts[num] > n // 3:
                result.append(num)
        
        return result
