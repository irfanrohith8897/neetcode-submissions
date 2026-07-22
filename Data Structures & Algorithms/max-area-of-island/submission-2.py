class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxArea=0
        d=((0,1),(1,0),(-1,0),(0,-1))
        rows=len(grid)
        cols=len(grid[0])

        def solve(i,j):
            visited[i][j]=True
            area=1
            for r,c in d:
                nr=i+r
                nc=j+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=0 and not visited[nr][nc]:
                    area+=solve(nr,nc)
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0 and not visited[i][j]:
                    maxArea=max(maxArea,solve(i,j))
        return maxArea