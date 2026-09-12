class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
                continue
            if i == 1:
                ans.append([1,1])
                continue
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                    continue
                temp.append(ans[i-1][j-1]+ans[i-1][j])
            
            ans.append(temp)
        return ans

