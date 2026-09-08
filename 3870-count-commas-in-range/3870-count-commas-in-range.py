class Solution:
    def countCommas(self, n: int) -> int:
        num = n - 999
        if num <= 0:
            return 0
        else:
            return num