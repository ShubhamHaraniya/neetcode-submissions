# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        p1 = l1
        p2 = l2
        carry = 0
        while p1 is not None and p2 is not None:
            s = p1.val + p2.val + carry
            need = s % 10
            carry = s // 10
            p1 = p1.next
            p2 = p2.next
            tail.next = ListNode(need)
            tail = tail.next
        
        while p1 is not None:
            s = p1.val + carry
            need = s % 10
            carry = s // 10
            p1 = p1.next
            tail.next = ListNode(need)  
            tail = tail.next

        while p2 is not None:
            s = p2.val + carry
            need = s % 10
            carry = s // 10
            p2 = p2.next
            tail.next = ListNode(need)   
            tail = tail.next   

        if carry is not 0:
            tail.next = ListNode(carry)
          
        return dummy.next