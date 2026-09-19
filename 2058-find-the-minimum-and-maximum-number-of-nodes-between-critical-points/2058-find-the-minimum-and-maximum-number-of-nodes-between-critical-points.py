# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        curr = head.next
        prev = head
        
        ans = [float('inf'),float('-inf')]

        points = []

        count = 1

        while curr and curr.next:
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if len(points) == 0:
                    points.append(count)
                else:
                    ans = [min(count - points[-1],ans[0]),max(count - points[0],ans[1])]
                    points.append(count)
            prev = curr
            curr = curr.next
            count += 1       
        
        if len(points) <= 1:
            return [-1,-1]
        return ans