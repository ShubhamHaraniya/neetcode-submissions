class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []

        def rec(idx, temp):
            if idx == len(nums):
                result.append(temp.copy())
                return

            temp.append(nums[idx])
            rec(idx + 1, temp)
            temp.pop()

            next_idx = idx + 1
            while next_idx < len(nums) and nums[next_idx] == nums[idx]:
                next_idx += 1

            rec(next_idx, temp)

        rec(0, temp)

        return result