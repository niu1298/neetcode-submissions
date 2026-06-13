class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        
        best = nums[0]
        curr = nums[0]

        for i in range(1,n):
            curr = max(nums[i],curr + nums[i])
            best = max(curr,best)
        
        return best