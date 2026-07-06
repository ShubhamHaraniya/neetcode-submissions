class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count =  1
        last  = 0
        for i in range(1,len(intervals)):
            if intervals[last][0] == intervals[i][0]:
                if intervals[last][1] <=  intervals[i][1]:
                    last = i
                    continue
            else:
                if intervals[last][1] >=  intervals[i][1]:
                    continue
            last = i
            count += 1
        return count