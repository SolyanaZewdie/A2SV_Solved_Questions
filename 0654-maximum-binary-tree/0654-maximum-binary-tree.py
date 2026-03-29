# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
    
        max_val = max(nums)
        index = nums.index(max_val)
    
        root = TreeNode(max_val)
    
        left_part = nums[:index]
        root.left = self.constructMaximumBinaryTree(nums[:index])
    
        right_part = nums[index + 1:]
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])
    
        return root
