class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []

        def rec(idx,temp):

            if idx == len(s):
                result.append(temp.copy())
            
            for i in range(idx+1,len(s)+1):
                if s[idx:i] == s[idx:i][::-1]:
                    temp.append(s[idx:i])
                    rec(i,temp)
                    temp.pop()
        
        rec(0,[])

        return result