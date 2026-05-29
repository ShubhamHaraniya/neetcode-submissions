class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = []
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            temp = [strs[i]]
            seen.append(strs[i])
            for j in range(i+1,len(strs)):
                if sorted(strs[j]) == sorted(strs[i]):
                    seen.append(strs[j])
                    temp.append(strs[j])
            result.append(temp)
        return result