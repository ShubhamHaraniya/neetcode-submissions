class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        main = [1 if ch in vowels else 0 for ch in s]
        count = sum(main[:k])
        out = count
        for i in range(1,len(main)-k+1):
            if out == k:
                return out
            count += (main[i+k-1] - main[i-1])
            out = max(out,count)
        return out