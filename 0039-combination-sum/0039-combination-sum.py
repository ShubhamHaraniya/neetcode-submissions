class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        temp = []
        def rec(idx,ri,temp):
            if ri == 0:
                result.append(temp.copy())
                return
            if idx == len(candidates):
                return
            
            if candidates[idx] <= ri:
                temp.append(candidates[idx])
                rec(idx,ri-candidates[idx],temp)
                temp.pop()
            rec(idx+1,ri,temp)

        rec(0,target,temp)

        return result    