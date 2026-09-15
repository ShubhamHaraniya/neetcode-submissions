class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []

        def rec(idx,temp,r):
            if r == 0:
                result.append(temp.copy())
                return

            if idx == len(candidates):
                return
            
            if candidates[idx] <= r:
                
                temp.append(candidates[idx])
                rec(idx,temp,r-candidates[idx])
                temp.pop()
            
            rec(idx+1,temp,r)
        
        rec(0,[],target)

        return result