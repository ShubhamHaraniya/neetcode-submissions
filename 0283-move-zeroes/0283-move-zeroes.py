class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left,right = 0,1
        while (right < len(nums)) and (left < len(nums)):
            while left < len(nums)-1 and nums[left] != 0:
                left += 1
            right = left
            while right < len(nums)-1 and nums[right] == 0:
                right += 1
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right += 1