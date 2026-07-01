class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m,start = sum(nums[:k]),sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            start = start + nums[i+k-1] - nums[i-1]
            m  = max(m,start) 
        
        return m /  k