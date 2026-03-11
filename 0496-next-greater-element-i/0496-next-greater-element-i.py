class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums1:
            index = nums2.index(n)
            next_greater = -1
            for j in range(index + 1, len(nums2)):
                if nums2[j] > n:
                    next_greater = nums2[j]
                    break
            result.append(next_greater)
        return result