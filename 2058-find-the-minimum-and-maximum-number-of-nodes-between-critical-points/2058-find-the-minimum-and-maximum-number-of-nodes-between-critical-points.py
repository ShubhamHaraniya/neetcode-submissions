# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        idx = 1  # 1-based index of `curr`

        while curr.next:
            # Check for local maxima or local minima
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                
                prev_idx = idx

            prev = curr
            curr = curr.next
            idx += 1

        # If fewer than 2 critical points were found
        if first_idx == prev_idx:
            return [-1, -1]

        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]