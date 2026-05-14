class Solution:

    def isSameSquare(self, position, other_position) -> bool:
        return math.floor(position[0] / 3) == math.floor(other_position[0] / 3) and math.floor(position[1] / 3) == math.floor(other_position[1] / 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hashmap = {k: [] for k in range(1, 10)}

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".": hashmap[int(board[row][col])].append([row, col])
        
        for key in hashmap:
            positions = hashmap[key]
            for position in positions:
                for other_position in positions:
                    if position != other_position:
                        if position[0] == other_position[0] or position[1] == other_position[1] or self.isSameSquare(position, other_position):
                            return False
        
        return True