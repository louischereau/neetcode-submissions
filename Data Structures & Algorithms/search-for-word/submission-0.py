class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        HEIGHT = len(board)
        WIDTH = len(board[0])

        def dfs(pos, index):
            if index == len(word):
                return True

            r, c = pos
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < HEIGHT and 0 <= nc < WIDTH and board[nr][nc] == word[index]:
                    board[nr][nc] = "#"           # mark visited
                    if dfs((nr, nc), index + 1):
                        board[nr][nc] = word[index]  # restore before returning
                        return True
                    board[nr][nc] = word[index]   # restore on backtrack

            return False

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if board[i][j] == word[0]:
                    board[i][j] = "#"             # mark starting cell
                    if dfs((i, j), 1):            # start matching from index 1
                        board[i][j] = word[0]     # restore before returning
                        return True
                    board[i][j] = word[0]         # restore on backtrack

        return False