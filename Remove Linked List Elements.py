# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        tam = ListNode(0)
        tam.next = head
        nodetruoc = tam
        nodeXet = head
        while nodeXet:
            if nodeXet.val == val:
                nodetruoc.next = nodeXet.next
            else:
                nodetruoc = nodeXet
            nodeXet = nodeXet.next
        return tam.next