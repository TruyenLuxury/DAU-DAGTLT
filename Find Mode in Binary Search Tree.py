# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import defaultdict
        count = defaultdict(int)
        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_freq = max(count.values())
        result = []

        for key in count:
            if count[key] == max_freq:
                result.append(key)
        return result