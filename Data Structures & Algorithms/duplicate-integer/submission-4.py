class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = []
        for i in nums:
            if i not in dic:
                dic.append(i)
            else:
                return True
        return False
