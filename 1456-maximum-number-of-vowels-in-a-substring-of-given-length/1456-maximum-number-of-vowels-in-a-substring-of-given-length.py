class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        out = 0
        r = 0

        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    r += 1
                    out = max(out,r)            
            else:
                if s[i] in vowels and s[i-k] in vowels:
                    continue
                elif s[i] in vowels:
                    r += 1
                    out = max(out,r)
                elif s[i-k] in vowels:
                    r -= 1
                else:
                    continue

        return out