class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i in range(len(spells)):
            m = len(potions)
            l,r =  0,m-1
            while l <= r:
                mid = (l+r)//2
                if spells[i]*potions[mid] >=  success:
                    r = mid - 1
                else:
                    l = mid + 1
            spells[i] = m - l
        return spells