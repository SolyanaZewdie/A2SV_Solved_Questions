# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            current_path = left + right + node.val

            if current_path > self.max_sum:
                self.max_sum = current_path

            return max(left, right) + node.val

        dfs(root)
        return self.max_sum