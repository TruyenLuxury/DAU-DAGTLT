# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:# Nếu node hiện tại là một lá (không có con nào), kiểm tra xem nó có phải là lá bên trái không
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False) # Đệ quy cho cả hai con, đánh dấu con bên trái là True và con bên phải là False
        return dfs(root, False)