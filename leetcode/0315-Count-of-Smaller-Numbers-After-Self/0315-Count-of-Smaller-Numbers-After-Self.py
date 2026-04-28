class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        enums = list(enumerate(nums)) 
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            l_ptr = 0
            r_ptr = 0
            right_count = 0 
            
            while l_ptr < len(left) and r_ptr < len(right):
                if right[r_ptr][1] < left[l_ptr][1]:
                    merged.append(right[r_ptr])
                    right_count += 1
                    r_ptr += 1
                else:
                    
                    ans[left[l_ptr][0]] += right_count
                    merged.append(left[l_ptr])
                    l_ptr += 1
            
            while l_ptr < len(left):
                ans[left[l_ptr][0]] += right_count
                merged.append(left[l_ptr])
                l_ptr += 1
            
            while r_ptr < len(right):
                merged.append(right[r_ptr])
                r_ptr += 1
                
            return merged

        merge_sort([(i, v) for i, v in enumerate(nums)])
        return ans