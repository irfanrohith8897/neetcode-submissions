from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append((i,j))
        d=((0,1),(1,0),(-1,0),(0,-1))
        while queue:
            i,j=queue.popleft()
            for dr,dc in d:
                nr=i+dr
                nc=j+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==2147483647:
                    grid[nr][nc]=grid[i][j]+1
                    queue.append((nr,nc))
        
