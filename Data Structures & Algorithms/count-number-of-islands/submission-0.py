class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    # run BFS here
                    visited.add((r,c))
                    queue = deque([(r,c)])
                    order = []

                    while queue:
                        cr, cc = queue.popleft()
                        order.append(cr)
                        order.append(cc)

                        for dr, dc in directions:
                            nr, nc, = cr + dr, cc + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
        
        return count