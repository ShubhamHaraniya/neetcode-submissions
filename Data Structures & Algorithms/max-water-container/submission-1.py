class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        maxi = 0
        while low < high:
            maxi =  max((min(heights[low],heights[high])*(high-low)),maxi)
            
            if heights[low] < heights[high]:
                low += 1
            elif heights[low] >= heights[high]:
                high -= 1
        return maxi