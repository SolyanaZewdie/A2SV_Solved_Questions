class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n=len(nums)
        diff=[0]*(n+1)
        
        for l,r in requests:
            diff[l]+=1
            diff[r+1]-=1
        
        freq=[0]*n
        cur=0
        for i in range(n):
            cur+=diff[i]
            freq[i]=cur
        
        nums.sort()
        freq.sort()
        
        mod=10**9+7
        ans=0
        
        for i in range(n):
            ans=(ans+nums[i]*freq[i])%mod
        
        return ans