class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix = 0
        seen = {0: -1}
        
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % k
            
            if prefix in seen:
                if i - seen[prefix] >= 2:
                    return True
            else:
                seen[prefix] = i
        
        return False
