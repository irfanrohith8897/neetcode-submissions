class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxArea=0
        def solve(i,j,area):
            visited[i][j]=True
            area=1
            d=((0,1),(1,0),(-1,0),(0,-1))
            for r,c in d:
                nr=i+r
                nc=j+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]!=0 and not visited[nr][nc]:
                    area+=solve(nr,nc,0)
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and not visited[i][j]:
                    maxArea=max(maxArea,solve(i,j,0))
        return maxArea