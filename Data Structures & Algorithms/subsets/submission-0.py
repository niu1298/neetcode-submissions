class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]
        elif n == 1:
            return [[],nums]
        elif n == 2:
            return [[],[nums[0]],[nums[1]],nums]
        else:
            ans = self.subsets(nums[:-1])
            addnum = [nums[-1]]
            ans.append(addnum)
            for item in ans[1:-1]:
                ans.append(item + addnum)
            return ans