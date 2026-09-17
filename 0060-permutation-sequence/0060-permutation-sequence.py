from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = list(range(1, n + 1))
        k -= 1
        result = []

        def rec(i, k):
            if i == 0:
                return

            f = factorial(i - 1)
            idx = k // f

            result.append(str(digits[idx]))
            digits.pop(idx)

            k %= f

            rec(i - 1, k)

        rec(n, k)

        return ''.join(result)