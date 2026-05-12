# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')# Khởi tạo min_diff với giá trị vô cùng lớn để đảm bảo rằng bất kỳ sự khác biệt nào tìm thấy sẽ nhỏ hơn giá trị này
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                diff = node.val - self.prev
                self.min_diff = min(self.min_diff, diff) # Cập nhật min_diff nếu diff hiện tại nhỏ hơn min_diff
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff