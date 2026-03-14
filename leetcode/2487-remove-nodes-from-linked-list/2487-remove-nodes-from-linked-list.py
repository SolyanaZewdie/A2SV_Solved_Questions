# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        head=prev
        maxv=0
        cur=head
        prev=None
        
        while cur:
            if cur.val>=maxv:
                maxv=cur.val
                prev=cur
                cur=cur.next
            else:
                prev.next=cur.next
                cur=cur.next
        
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        
        return prev