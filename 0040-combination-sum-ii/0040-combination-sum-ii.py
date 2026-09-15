class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
    
        candidates.sort()

        result = []

        def rec(idx,temp,r):
            if r == 0:
                result.append(temp.copy())
                return

            if idx == len(candidates):
                return

            if r <  0:
                return
            
            temp.append(candidates[idx])

            rec(idx+1,temp,r-candidates[idx])

            temp.pop()
            
            next_idx = idx + 1

            while next_idx < len(candidates):
                if candidates[next_idx] != candidates[idx]:
                    break
                next_idx += 1
             
            rec(next_idx,temp,r)
        
        rec(0,[],target)

        return result