class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        curr_num = nums[0]
        for num in nums:
            if num == curr_num:
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                curr_num = num
                counter = 1
        return curr_num