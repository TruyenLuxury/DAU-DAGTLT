# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(node):# Hàm đệ quy để thực hiện duyệt theo thứ tự Inorder (Left, Root, Right)
            if not node:
                return
            inorder(node.left)   # Left
            result.append(node.val)  # Root
            inorder(node.right)  # Right
        inorder(root)
        return result