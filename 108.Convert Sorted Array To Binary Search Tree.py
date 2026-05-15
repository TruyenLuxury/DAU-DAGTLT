# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])# Đệ quy xây dựng cây con bên trái từ nửa đầu của mảng
        root.right = self.sortedArrayToBST(nums[mid+1:])# Đệ quy xây dựng cây con bên phải từ nửa sau của mảng
        return root