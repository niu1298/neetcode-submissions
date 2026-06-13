class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        if n ==0:
            return [newInterval]

        ans = intervals[:]
        ans.append(newInterval)
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

        # for i in range(len(intervals)):
        #     s,e = intervals[i][0],intervals[i][1]
        #     if start < s and end < s:
        #         ans.insert(i,newInterval)
        #         return ans
        #     if start < s and end > s:
        #         if end < e:
        #             ans[i] = [start, e]
        #             return ans
        #         else:
        #             ans[i][0] = start
        #             start = 
        #             continue
