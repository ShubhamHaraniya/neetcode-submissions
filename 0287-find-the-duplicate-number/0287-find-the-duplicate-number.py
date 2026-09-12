class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # dict = defaultdict(int)
        # for num in nums:
        #     if dict[num] == 0:
        #         dict[num] += 1
        #     else:
        #         return num        

        slow = nums[0]
        fast = nums[nums[0]]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow