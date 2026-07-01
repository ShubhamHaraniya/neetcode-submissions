from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0
        seen = defaultdict(int)
        for num in nums:
            w = k - num
            if seen[w] >  0:
                seen[w] -= 1
                op += 1
                continue
            seen[num] += 1
        return op