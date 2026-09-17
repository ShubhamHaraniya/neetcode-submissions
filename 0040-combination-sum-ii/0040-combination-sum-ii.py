class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
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
                rec(idx+1,ri-candidates[idx],temp)
                temp.pop()
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1
            rec(next_idx,ri,temp)

        rec(0,target,temp)

        return result    