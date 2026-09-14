# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow,fast = head,head
        p = head
        l = 0
        if not head:
            return None
        while p is not None:
            p = p.next
            l += 1
        if k % l == 0:
            return head
        for i in range(k%l):
            fast = fast.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        slow.next = None

        p = temp

        while p is not None and p.next is not None:
            p = p.next

        p.next = head

        return temp 