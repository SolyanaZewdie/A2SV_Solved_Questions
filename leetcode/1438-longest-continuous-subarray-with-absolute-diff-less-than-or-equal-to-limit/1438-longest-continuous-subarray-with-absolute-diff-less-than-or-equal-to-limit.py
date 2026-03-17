class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxd = deque()
        mind = deque()
        l = 0
        ans = 0

        for r, v in enumerate(nums):
            while maxd and v > maxd[-1]: 
                maxd.pop()
            while mind and v < mind[-1]: 
                mind.pop()

            maxd.append(v)
            mind.append(v)

            while maxd[0] - mind[0] > limit:
                if nums[l] == maxd[0]: 
                    maxd.popleft()
                if nums[l] == mind[0]: 
                    mind.popleft()
                l += 1

            ans = max(ans, r - l + 1)

        return ans
        