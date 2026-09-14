class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                l = max(l,temp)
            else:
                temp = 0
        return l