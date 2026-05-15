# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val# Nếu node hiện tại là một node lá (không có con trái và con phải), thì kiểm tra xem giá trị của node có bằng targetSum hay không. Nếu bằng, trả về True, ngược lại trả về False.
        targetSum -= root.val
        return (self.hasPathSum(root.left,targetSum)) or (self.hasPathSum(root.right,targetSum))