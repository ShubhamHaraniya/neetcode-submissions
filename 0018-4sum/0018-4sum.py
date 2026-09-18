class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s2 = nums[i] + nums[j]
                rei = target - s2
                low,high = j+1,len(nums)-1
                while low < high:
                    if nums[low] + nums[high] == rei:
                        if [nums[i], nums[j], nums[low], nums[high]] in result:
                            low += 1
                            high -= 1
                            continue
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > rei:
                        high -= 1
                    else:
                        low += 1
        return result