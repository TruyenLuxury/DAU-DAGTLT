# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        start = head
        prev = None
        end = None
        while head:
            head.prev = prev # build
            prev = head     # update new
            head = head.next # move
        end = prev

        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.prev
        
        return True