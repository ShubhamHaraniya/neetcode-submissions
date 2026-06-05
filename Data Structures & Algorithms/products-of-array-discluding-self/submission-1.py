class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  
        prefix = [1] * n
        postfix  = [1] * n

        for i in range(n):
            if i == 0:
                prefix[i] = 1
                postfix[-(i+1)] == 1
            else:
                prefix[i] *= (prefix[i-1] * nums[i-1])
                postfix[-(i+1)] *= ( postfix[-i] * nums[-i])
        
        return [x * y for x, y in zip(prefix, postfix, strict=True)]