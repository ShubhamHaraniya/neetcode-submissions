class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def rec(idx,nums):
            if idx == len(nums):
                result.append(nums.copy())
                return 
            
            for i in range(idx,len(nums)):
                nums[idx],nums[i] = nums[i],nums[idx]
                rec(idx+1,nums)
                nums[idx],nums[i] = nums[i],nums[idx]
        
        rec(0,nums)
        return result