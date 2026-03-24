class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        
        def dfs(l, r):
            if l == r:
                return nums[l]
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            pick_left = nums[l] - dfs(l + 1, r)
            pick_right = nums[r] - dfs(l, r - 1)
            
            memo[(l, r)] = max(pick_left, pick_right)
            return memo[(l, r)]
        
        return dfs(0, len(nums) - 1) >= 0