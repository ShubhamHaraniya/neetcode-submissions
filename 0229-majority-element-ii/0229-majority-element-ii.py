class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        c1 , c2 = None,None
        p1,p2 = 0,0

        for num in nums:
            if num == c1:
                p1 += 1
            elif num == c2:
                p2 += 1
            elif p1 == 0:
                c1 = num
                p1 += 1
            elif p2 == 0:
                c2  = num
                p2 += 1
            else:
                p1 -= 1
                p2 -= 1

        return [x for x in (c1,c2) if nums.count(x) > len(nums)//3]