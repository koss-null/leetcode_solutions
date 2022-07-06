# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None

        cur = head
        prev_val = cur.val
        prev = cur
        while cur is not None:
            while cur and cur.val == prev_val:
                cur = cur.next
            prev.next = cur
            prev_val = cur.val if cur else None
            prev = cur
            if cur:
                cur = cur.next
        return head
        