class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        m=0
        for x in nums:
            s+=x
            if s<m:
                m=s
        if m<0:
            return 1-m
        return 1