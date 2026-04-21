class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums1)
        arr = [nums1[i] - nums2[i] for i in range(n)]
        
        def merge_sort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and arr[i] > arr[j] + diff:
                    j += 1
                count += (right - j + 1)
            
            temp = []
            l, r = left, mid + 1
            
            while l <= mid and r <= right:
                if arr[l] <= arr[r]:
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[r])
                    r += 1
            
            while l <= mid:
                temp.append(arr[l])
                l += 1
            
            while r <= right:
                temp.append(arr[r])
                r += 1
            
            for i in range(len(temp)):
                arr[left + i] = temp[i]
            
            return count
        
        return merge_sort(0, n - 1)        