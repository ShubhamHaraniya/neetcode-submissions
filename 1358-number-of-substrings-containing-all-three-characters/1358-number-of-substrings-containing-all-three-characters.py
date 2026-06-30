class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        cnt = {'a': 0, 'b': 0, 'c': 0}

        for j in range(len(s)):
            cnt[s[j]] += 1

            while cnt['a'] and cnt['b'] and cnt['c']:
                ans += len(s) - j
                cnt[s[i]] -= 1
                i += 1

        return ans