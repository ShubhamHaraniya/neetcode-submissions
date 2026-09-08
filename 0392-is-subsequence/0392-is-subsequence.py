class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n  = len(t)
        if m == 0: return True
        if m > n: return False

        j = 0
        for i in range(n):
            if t[i] == s[j]:
                if j == m-1:
                    return True
                j += 1
        return False