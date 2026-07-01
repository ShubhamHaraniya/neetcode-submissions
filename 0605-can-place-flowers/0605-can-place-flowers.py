class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        r = 1
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] ==  0:
                return True
        while r<len(flowerbed):
            if (r-1  == 0 or r == len(flowerbed)-1):
                if flowerbed[r] == 0 and flowerbed[r-1] ==  0:
                    flowerbed[r-1] = 1
                    n -= 1 
            else :
                if (flowerbed[r-2] == 0 and flowerbed[r] == 0 and flowerbed[r-1] ==  0):
                    flowerbed[r-1] = 1
                    n -= 1
            if n == 0:
                return True
            r += 1
        return False