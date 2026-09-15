class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1: mid -= 1   # force mid to even index
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2   # pair intact -> single is to the right
            else:
                hi = mid       # pair broken -> single is here or left
        return nums[lo]