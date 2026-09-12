# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        ans = ListNode(head.val)
        while current.next is not None:
            current = current.next
            temp = ListNode(current.val)
            temp.next = ans
            ans = temp
        return ans

        