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



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        curr = []

        def dfs(open_c, close_c):
            if open_c+ close_c == 2*n:
                ans.append("".join(curr))
                return
            if open_c < n:
                curr.append("(")
                dfs(open_c+1, close_c)
                curr.pop()
                # return
            if close_c < open_c:
                curr.append(")")
                dfs(open_c, close_c + 1)
                curr.pop()
                # return
            
        dfs(0,0)
        return ans
            