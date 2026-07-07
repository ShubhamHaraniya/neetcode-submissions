class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        out = []
        for i in spells:
            l,r =  0,len(potions)-1
            while l <= r:
                mid = (l+r)//2
                if i*potions[mid] >=  success:
                    r = mid - 1
                else:
                    l = mid + 1
            out.append(len(potions)-l)
        return out