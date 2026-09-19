from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        result = 0
        for num in nums:
            target = k - num
            if dic[target] != 0:
                result += 1
                dic[target] -= 1
            else:
                dic[num] += 1
        return result