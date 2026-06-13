from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        n = len(nums)

        for i in range(n):
            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

            if maxReach >= n - 1:
                return True

        return True

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n == 1:
#             return True

#         path = []
#         def dfs(curr):
#             if curr == n-1:
#                 return True
            
#             if nums[curr] == 0:
#                 return False
            
#             for i in range(nums[curr],0,-1):
#                 if curr+i<n and dfs(curr+i):
#                     return True
            
#             return False

#         return dfs(0)
