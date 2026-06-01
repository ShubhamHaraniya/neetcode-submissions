class Solution:
    def maxArea(self, heights: List[int]) -> int:
        storage = 0
        for i,num in enumerate(heights):
            for j in range(i+1,len(heights)):
                storage = max(min(num,heights[j])*(j-i),storage)
        return storage