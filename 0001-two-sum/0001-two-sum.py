class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = {}

        for i,num in enumerate(nums):
            if (target - num) in n.keys():
                return [n[target-num],i]
            else:
                n[num] = i 
    