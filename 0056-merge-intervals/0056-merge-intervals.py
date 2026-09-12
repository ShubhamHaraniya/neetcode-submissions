class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        re = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] > re[-1][0]:
                if intervals[i][0] <= re[-1][1]:
                    re[-1][1] = max(re[-1][1],intervals[i][1])
                else : re.append(intervals[i])
            else:
                if intervals[i][1] < re[-1][1]:
                    continue
                else:
                    re[-1][1] = intervals[i][1]      
        return re