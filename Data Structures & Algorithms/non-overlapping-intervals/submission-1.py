class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # n = len(intervals)
        # if n ==1:
        #     return 0
        intervals.sort(key = lambda p :p[1])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1,len(intervals)):
            s,e = intervals[i]
            if s < prev_end:
                count += 1
            else:
                prev_end = e
                # continue
        
        return count