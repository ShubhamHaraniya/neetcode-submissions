class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right = 0,0
        delete = 1
        out = 0
        while right < len(nums):
            if (nums[right] == 1):
                out = max(out,right-left+delete)
            else:
                if delete != 0:
                    point = right + 1
                    delete -= 1 
                else:
                    delete = 1
                    left,right = point,point
                    continue
            right += 1
        if out == len(nums):
            return out - 1
        else:
            return out