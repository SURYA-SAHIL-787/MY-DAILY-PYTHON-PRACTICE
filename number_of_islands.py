from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = [(r, c)]
            visit.add((r, c))
            
            while q:
                row, col = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nxt_r, nxt_c = row + dr, col + dc
                    if (0 <= nxt_r < rows and 
                        0 <= nxt_c < cols and 
                        grid[nxt_r][nxt_c] == "1" and 
                        (nxt_r, nxt_c) not in visit):
                        q.append((nxt_r, nxt_c))
                        visit.add((nxt_r, nxt_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid))  # Output: 3
