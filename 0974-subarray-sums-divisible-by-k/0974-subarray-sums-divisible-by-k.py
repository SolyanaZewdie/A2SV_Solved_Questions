class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        s=0
        ans=0
        for x in nums:
            s+=x
            r=s%k
            if r in freq:
                ans+=freq[r]
                freq[r]+=1
            else:
                freq[r]=1
        return ans