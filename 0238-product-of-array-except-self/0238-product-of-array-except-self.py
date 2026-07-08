class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefix[i] = nums[i-1] * prefix[i-1]
                postfix[-i - 1] = nums[-i] * postfix[-i]
        
        return [i*j for i,j in  zip(prefix,postfix)]

        