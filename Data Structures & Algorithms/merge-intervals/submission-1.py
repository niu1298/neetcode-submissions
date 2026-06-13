class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        if n ==1:
            return intervals

        ans = intervals[:]
        # ans.append(newInterval)
        ans.sort()

        curr_pos = 1
        while curr_pos<len(ans):
            i = curr_pos
            if ans[i][0] <= ans[i-1][1]:
                ans[i-1] = [min(ans[i-1] + ans[i]),max(ans[i-1]+ans[i])]
                del ans[i]
                # print(ans)
            else:
                curr_pos += 1
        
        return ans