class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        rank = {}
        
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in rank:
                rank[sorted_nums[i]] = i
        
        result = []
        for num in nums:
            result.append(rank[num])
        
        return result
