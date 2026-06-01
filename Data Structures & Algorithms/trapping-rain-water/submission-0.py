class Solution:
    def trap(self, height: List[int]) -> int:
        store = 0
        i = 0
        while i < len(height) - 1:
            if height[i] == 0 or (height[i+1] >= height[i]):
                i += 1
                continue
            else:
                flag = False
                trap = 0
                for j in range(i+1, len(height)):
                    if height[j] >= height[i]:
                        store += (height[i] * (j - i - 1) - trap)
                        i = j
                        flag = True
                        break
                    else:
                        trap += height[j]
                if flag:
                    continue
                else:

                    height[i] -= 1
        return store