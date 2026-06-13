# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:

#         map = dict()

#         map[1] = ["()"]
#         map[2] = ["()()","(())"]

#         def dfs(m):
#             if m in map:
#                 return map[m]

#             curr_li = dfs(m-1)

#             li = []

#             for st in curr_li:
#                 for i in range(len(st)+1):
#                     temp = st[:i] + "()" + st[i:]
#                 # com = [st+"()","(" + st + ")", "()" + st]

#                 # for temp in com:
#                     if temp not in li:
#                         li.append(temp)
            
#             map[m] = li

#             return li

#         ans = dfs(n)
#         ans.sort()

#         return ans

# from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []

        def dfs(open_count, close_count):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return

            if open_count < n:
                curr.append("(")
                dfs(open_count + 1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(")")
                dfs(open_count, close_count + 1)
                curr.pop()

        dfs(0, 0)
        return ans