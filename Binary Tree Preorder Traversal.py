# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if not node:
                return 0
            result.append(node.val)# Thêm giá trị của node hiện tại vào danh sách kết quả trước khi tiếp tục duyệt cây con bên trái và bên phải.
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result