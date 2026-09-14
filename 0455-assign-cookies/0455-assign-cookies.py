class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j, count = 0,0
        for i in range(len(s)):
            if j < len(g) and g[j] <= s[i]:
                count += 1
                j += 1
            if j == len(g):
                break
        return count