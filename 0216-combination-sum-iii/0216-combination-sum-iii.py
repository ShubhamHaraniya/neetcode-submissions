class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        digits = [i+1 for i in range(9)]
        result = []
        
        def rec(idx,rei_char,rei_sum,temp):
            if rei_char == 0 and rei_sum == 0:
                result.append(temp.copy())
                return
            if rei_char == 0 or idx == len(digits):
                return
            
            if digits[idx] <= rei_sum:
                temp.append(digits[idx])
                rec(idx+1,rei_char - 1,rei_sum - digits[idx],temp)
                temp.pop()
            rec(idx+1,rei_char,rei_sum,temp)
        
        rec(0,k,n,[])

        return result