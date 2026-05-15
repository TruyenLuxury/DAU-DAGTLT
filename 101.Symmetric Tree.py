# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(left,right):
            if not left and not right:# Nếu cả hai cây con đều rỗng, chúng đối xứng với nhau
                return True
            if not left or not right:# Nếu một trong hai cây con rỗng và cái còn lại không rỗng, chúng không đối xứng
                return False
            if left.val != right.val:# Nếu giá trị của hai nút không bằng nhau, chúng không đối xứng
                return False
            return check(left.left, right.right) and check(left.right, right.left)# Đệ quy kiểm tra tính đối xứng của các cây con bên trái và bên phải
        return check(root.left, root.right)