class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = []

        def dfs(start, path, total):
            if total == target:
                ans.append(path[:])
                return

            # elif total > target:
            #     return

            for i in range(start, len(nums)):
                
                if total + nums[i] > target:
                    break

                path.append(nums[i])
                dfs(i, path, total + nums[i])
                path.pop()

        dfs(0,[],0)

        return ans
