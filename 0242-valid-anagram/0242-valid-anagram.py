from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for c in s:
            sd[c] += 1
        for c in t:
            td[c] += 1
        return sd == td