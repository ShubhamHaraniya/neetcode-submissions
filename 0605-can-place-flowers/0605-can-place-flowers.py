class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n == 0:
                return True
            elif n == 1:
                if flowerbed[0] ==0:
                    return True
                else:
                    return False
            else:
                return False

        for i in range(len(flowerbed)):
            if n == 0:
                return True
                
            if i == 0:
                if flowerbed[i+1] != 1 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
                continue
            if i == len(flowerbed) - 1 and flowerbed[i] == 0:
                if flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1
                continue
            if i == len(flowerbed) - 1:
                continue
            if flowerbed[i+1] == 0 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
        return True if n == 0 else False