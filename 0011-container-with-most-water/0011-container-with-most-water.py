class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0, len(height) -1
        most = 0
        while l<r:
            most = max(most,min(height[l],height[r])*(r-l))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return most