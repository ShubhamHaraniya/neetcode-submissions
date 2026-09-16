class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        mini = float('inf')
        idx = i

        for j in range(i + 1, n):
            if nums[j] > nums[i] and nums[j] <= mini:
                mini = nums[j]
                idx = j

        nums[i], nums[idx] = nums[idx], nums[i]

        nums[i + 1:] = nums[i + 1:][::-1]