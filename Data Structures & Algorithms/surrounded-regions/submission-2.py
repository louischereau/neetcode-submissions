class Solution:
    def solve(self, board: List[List[str]]) -> None:

        HEIGHT, WIDTH = len(board), len(board[0])

        border_os = [
            (r, c)
            for r in range(HEIGHT)
            for c in range(WIDTH)
            if board[r][c] == 'O' and (r == 0 or r == HEIGHT-1 or c == 0 or c == WIDTH-1)
        ]

        visited = set(border_os)

        stack = list(border_os)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:
            cell = stack.pop()
            for dr, dc in directions:
                row = cell[0] + dr
                col = cell[1] + dc
                if 0 <= row < HEIGHT and 0 <= col < WIDTH and board[row][col]== 'O' and (row, col) not in visited:
                    visited.add((row, col))
                    stack.append((row, col))
        
        for r in range(HEIGHT):
            for c in range(WIDTH):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'





