class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0,head)
        slow = head
        fast =  head
        for i in range(n):
            fast = fast.next
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next
        
        slow.next = slow.next.next
    
        return head.next