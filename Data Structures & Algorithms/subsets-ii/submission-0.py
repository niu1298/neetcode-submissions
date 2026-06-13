class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # ans = set()
        # ans.add([])

        ans = []

        li = nums[:]
        li.sort()
        curr = []
        n = len(nums)

        def dfs(start):
            ans.append(curr.copy())

            if li == []:
                return

            if len(li) == 1:
                ans.append(li)
                return
            
            for i in range(start, n):
                # if i>start and li[i] == li[i-1]:
                #     continue
                temp = li[i]
                curr.append(temp)
                curr.sort()
                if curr in ans:
                    print(curr)
                    
                    curr.pop()
                    continue
                # ans.append(curr.copy())
                dfs(i+1)
                curr.pop()
                # del curr

        dfs(0)

        return list(ans)
