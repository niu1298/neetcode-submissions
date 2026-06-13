class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # curr_pos = [0,0]
        # x = 0
        # y = 0
        # # curr_num = 0
        li = []
        m,n = len(board), len(board[0])
        pos_s = []
        def dfs(x,y, curr_num):

            if (board[x][y] == word[curr_num]):
                li.append(board[x][y])
                pos_s.append([x,y])
                # print(board[x][y])
                # print(li)
                # print(len(word))
                # print(len(li))

                if "".join(li) == word:
                    return True

                for pos in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n and (pos not in pos_s):
                        if dfs(pos[0],pos[1],curr_num + 1):
                            return True
                        
                li.pop()
                pos_s.pop()
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        
        return False

            
        