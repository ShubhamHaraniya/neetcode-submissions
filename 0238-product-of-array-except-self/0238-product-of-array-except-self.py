class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            pre[i] = pre[i-1] * nums[i-1]
            post[i] = post[i-1] * nums[len(nums)-i]
        
        for i in range(len(nums)):
            nums[i] = post[len(nums)-i-1] * pre[i]
        
        return nums