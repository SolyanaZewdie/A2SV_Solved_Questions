class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.at_most(nums, k) - self.at_most(nums, k - 1)
    
    def at_most(self, nums, k):
        freq = {}
        left = 0
        count = 0
        
        for right in range(len(nums)):
            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1
            
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            count += right - left + 1
        
        return count
