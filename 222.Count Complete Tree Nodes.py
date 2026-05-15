# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        # tính chiều cao bên trái
        def getLeftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        # tính chiều cao bên phải
        def getRightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left = getLeftHeight(root)
        right = getRightHeight(root)

        if left == right:
            return (1 << left) - 1  # 2^h - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right) # Đếm node hiện tại + đếm node bên trái + đếm node bên phải 