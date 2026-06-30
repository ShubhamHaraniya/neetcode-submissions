class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        j = 2
        while j<len(s):
            if ('a' in s[i:j+1]) and ('b' in s[i:j+1]) and ('c' in s[i:j+1]):
                ans += 1 + (len(s)-j-1)
                i += 1
            else:
                j += 1
        return ans 