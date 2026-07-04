from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l = Counter(arr)
        return len(l.values()) == len(set(l.values()))