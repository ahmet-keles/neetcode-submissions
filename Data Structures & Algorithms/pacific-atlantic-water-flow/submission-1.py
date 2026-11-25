class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedP = set()
        visitedA = set()

        queueP = collections.deque()
        queueA = collections.deque()

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        ROWS = len(heights)
        COLS = len(heights[0])
        
        row = 0
        col = 0
        for col in range(COLS):
            queueP.append((row, col))
            visitedP.add((row, col))
        
        row = 0
        col = 0
        for row in range(ROWS):
            queueP.append((row, col))
            visitedP.add((row, col))

        row = ROWS-1
        col = 0
        for col in range(COLS):
            queueA.append((row, col))
            visitedA.add((row, col))


        row = 0
        col = COLS-1
        for row in range(ROWS):
            queueA.append((row, col))
            visitedA.add((row, col))

        while queueP:
            cr, cc = queueP.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[cr][cc] and (nr, nc) not in visitedP:
                    queueP.append((nr, nc))
                    visitedP.add((nr, nc))

        while queueA:
            cr, cc = queueA.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[cr][cc] and (nr, nc) not in visitedA:
                    queueA.append((nr, nc))
                    visitedA.add((nr, nc))
    
        res = list(visitedP & visitedA)

        return res