# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        from collections import deque
        if not root:
            return []
        result = []
        queue = deque([root])  # bắt đầu từ root
        while queue:
            level_size = len(queue)  # số node ở tầng hiện tại
            level_sum  = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                # Thêm con vào queue cho tầng tiếp theo
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / float(level_size))  # avg của tầng này
        return result