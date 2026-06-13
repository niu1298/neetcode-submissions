class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        grid = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1
        

        for summation in range(2, m+n-1):
            for i in range(summation):
                if i<m and i>0 and summation-i<n and summation-i>0:
                    grid[i][summation-i] = grid[i-1][summation-i] + grid[i][summation-i-1]

        return grid[m-1][n-1]
