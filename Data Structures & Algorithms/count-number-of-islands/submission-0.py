class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res=0
        def solve(i,j):
            visited[i][j]=True
            d=((0,1),(1,0),(-1,0),(0,-1))
            for r,c in d:
                nr=i+r
                nc=j+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]!="0" and not visited[nr][nc]:
                    solve(nr,nc)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="0" and not visited[i][j]:
                    solve(i,j)
                    res+=1
        return res