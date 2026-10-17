from typing import List

class Solution:        
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def backtrack(path: List[int]):
            # 1. Check if it's a valid solution (all queens placed)
            if len(path) == n:
                # Convert path (column indices) into the required List[str] board format
                board = []
                for c in path:
                    row_str = '.' * c + 'Q' + '.' * (n - c - 1)
                    board.append(row_str)
                res.append(board)
                return
                
            # Current row we are placing a queen in
            row = len(path)
            
            # Choices are columns 0 to n-1
            for col in range(n):
                # 2. Check if choice is promising (no column or diagonal conflicts)
                # conflict if: same column (c == col) or diagonal (|c - col| == row - r)
                if any(c == col or abs(c - col) == row - r for r, c in enumerate(path)):
                    continue
                    
                # 3. Choose
                path.append(col)
                
                # 4. Explore
                backtrack(path)
                
                # 5. Un-choose (Backtrack)
                path.pop()

        backtrack([])
        return res