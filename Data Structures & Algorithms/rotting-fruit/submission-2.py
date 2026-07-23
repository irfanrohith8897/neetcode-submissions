from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque([])
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        d=((0,1),(1,0),(-1,0),(0,-1))
        time=0
        rotten=0
        while queue:
            size=len(queue)
            is_rotten=False
            for _ in range(size):
                i,j=queue.popleft()
                for r,c in d:
                    nr=i+r
                    nc=j+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc))
                        is_rotten=True
                        rotten+=1
            if is_rotten:
                time+=1
        return time if time>=0 and rotten==fresh else -1
                
        
