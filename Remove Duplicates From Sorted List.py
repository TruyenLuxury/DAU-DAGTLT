# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
 #       self.val = val
 #       self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:# Nếu giá trị của node hiện tại bằng giá trị của node tiếp theo, bỏ qua node tiếp theo
                current.next = current.next.next
            else:# Nếu giá trị của node hiện tại khác giá trị của node tiếp theo, di chuyển current đến node tiếp theo
                current = current.next
        return head       