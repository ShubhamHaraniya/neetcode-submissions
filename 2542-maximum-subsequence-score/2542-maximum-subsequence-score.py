import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        running_sum = 0
        max_score = 0
        
        for b, a in pairs:
            heapq.heappush(heap, a)
            running_sum += a
            if len(heap) > k:
                running_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, running_sum * b)
                
        return max_score