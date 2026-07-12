class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        rank = {}

        for i, num in enumerate(temp):
            rank[num] = i + 1

        return [rank[num] for num in arr]