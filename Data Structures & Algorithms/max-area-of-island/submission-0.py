class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    count += 1
                    area = 1
                    # run BFS here
                    visited.add((r,c))
                    queue = deque([(r,c)])

                    while queue:
                        cr, cc = queue.popleft()

                        for dr, dc in directions:
                            nr, nc, = cr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                                area += 1
                    max_area = max(max_area, area)
        
        return max_area