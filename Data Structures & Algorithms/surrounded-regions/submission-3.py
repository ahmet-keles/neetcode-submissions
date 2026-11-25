class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        queue = collections.deque()
        col = 0
        row = 0
        for col in range(COLS):
            if board[row][col] == 'O':
                board[row][col] = 'M'
                queue.append((row, col))
        col = 0
        row = ROWS - 1
        for col in range(COLS):
            if board[row][col] == 'O':
                board[row][col] = 'M'
                queue.append((row, col))
        row = 0
        col = 0
        for row in range(ROWS):
            if board[row][col] == 'O':
                board[row][col] = 'M'
                queue.append((row, col))
        row = 0
        col = COLS - 1
        for row in range(ROWS):
            if board[row][col] == 'O':
                board[row][col] = 'M'
                queue.append((row, col))

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                    board[nr][nc] = 'M'
                    queue.append((nr, nc))
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'M':
                    board[row][col] = 'O'




