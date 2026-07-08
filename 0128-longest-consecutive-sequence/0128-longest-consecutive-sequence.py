class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l  = 0
        for n in s:
            if n-1 not in s:
                length = 1
                while n + length in s:
                    length += 1
                l = max(l,length)
        return l