class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i,num in enumerate(nums):
            if i != 0:
                if nums[i-1] == nums[i]:
                    continue
            target = -num
            low = i+1
            high = len(nums) - 1

            while low < high:
                result = nums[low] + nums[high]
                if result == target:
                    answer.append([num,nums[low],nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif result > target:
                    high -= 1
                else:
                    low += 1
        return answer