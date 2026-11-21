class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        res = 0

        while queue:
            cr, cc, minute = queue.popleft()
            for dr, dc in directions:
                nr, nc, = cr + dr, cc + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[cr]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, minute+1))
                    res = minute+1
        

        if any(1 in row for row in grid):
            return -1
        else:
            return res             
                    
                            