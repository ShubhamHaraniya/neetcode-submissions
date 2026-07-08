class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            r = target - n
            if r in seen:
                return [seen[r],i]
            else:
                seen[n] = i
        