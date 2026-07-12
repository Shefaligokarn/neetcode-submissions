class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or
                (r,c) in visit 
            ):
                return 0

            visit.add((r,c))


            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


        max_area = 0

        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r,c))

        return max_area
