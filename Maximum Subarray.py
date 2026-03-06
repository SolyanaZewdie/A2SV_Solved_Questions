class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=nums[0]
        best=nums[0]
        
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            best=max(best,cur)
        
        return best
