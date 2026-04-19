class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            minn = i
            for j in range(i+1, n):
                if nums[j] < nums[minn]:
                    minn = j
            nums[i], nums[minn] = nums[minn], nums[i]
        return nums