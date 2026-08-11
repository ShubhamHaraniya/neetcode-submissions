class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        si = set(nums)
        s = nums[0]
        for i in range(1,len(nums)):
            if nums[i] -1 == nums[i-1]:
                s += nums[i] 
            else:
                break 
        while True:
            if s not in si:
                return s 
            else:
                s += 1