# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            nextNode = curr.next # Lưu lại node tiếp theo trước khi thay đổi liên kết
            curr.next = prev # Đảo ngược liên kết
            prev = curr # Di chuyển prev lên curr
            curr = nextNode # Di chuyển curr lên node tiếp theo đã lưu
        return prev