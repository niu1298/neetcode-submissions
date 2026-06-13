# from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # 一个完整排列
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # 选择 nums[i]
                used[i] = True
                path.append(nums[i])

                backtrack()

                # 撤销选择
                path.pop()
                used[i] = False

        backtrack()
        return res