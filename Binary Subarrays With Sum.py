class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = {0:1}
        s = 0
        ans = 0

        for x in nums:
            s += x
            if s - goal in count:
                ans += count[s - goal]
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        return ans
