class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                multi[i] *= nums[j]
        return multi 