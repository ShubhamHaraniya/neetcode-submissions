class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # fact = 1
        # temp = n-1
        # while temp > 0:
        #     fact *= temp
        #     temp -= 1
        
        # digit = k // fact
        # rank = (k % fact) - 1

        # def rec()
        from math import factorial 
        digits = list(range(1, n+1))
        k -= 1       # 0-indexed
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            idx = k // f 
            result.append(str(digits[idx])) 
            digits.pop(idx)
            k %= f 
        return ''.join(result)