class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        # case 1
        li = nums[:-1]
        dp = [0 for i in range(len(li))]

        dp[0] = li[0]
        dp[1] = max(li[0],li[1])

        for i in range(2,len(li)):
            dp[i] = max(dp[i-1],dp[i-2]+li[i])

        ans1 = dp[-1]

        
        # case 2
        li = nums[1:]
        dp = [0 for i in range(len(li))]

        dp[0] = li[0]
        dp[1] = max(li[0],li[1])

        for i in range(2,len(li)):
            dp[i] = max(dp[i-1],dp[i-2]+li[i])

        ans2 = dp[-1]

        return max(ans1,ans2)