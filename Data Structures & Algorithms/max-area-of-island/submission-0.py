class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # counts = 0

        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        def dfs(r,c):
            nonlocal area
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == 0:
                return
            
            # if grid[r][c] == "1":
            #     area += 1
            
            grid[r][c] = 0

            area += 1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            # return ans 

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    if area > max_area:
                        max_area = area
        
        return max_area