# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if root == None:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            self.ans = max(self.ans, left_depth+right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.ans