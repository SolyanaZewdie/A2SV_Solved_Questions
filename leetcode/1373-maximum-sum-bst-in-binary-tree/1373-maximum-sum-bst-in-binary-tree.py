# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0

        def dfs(node):
            if node is None:
                return (True, 0, float('inf'), float('-inf'))

            left_isBST, left_sum, left_min, left_max = dfs(node.left)
            right_isBST, right_sum, right_min, right_max = dfs(node.right)

            if left_isBST and right_isBST and left_max < node.val < right_min:
                
                current_sum = left_sum + right_sum + node.val
                
                if current_sum > self.max_sum:
                    self.max_sum = current_sum

                return (
                    True,
                    current_sum,
                    min(left_min, node.val),
                    max(right_max, node.val)
                )

            else:
                return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum