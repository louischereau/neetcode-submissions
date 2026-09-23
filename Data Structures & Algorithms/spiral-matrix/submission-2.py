class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [matrix[0][0]]
        visited = set([(0, 0)])
        n, m = len(matrix), len(matrix[0])
        px, py = 0, 0

        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        spiral_directions = [RIGHT, DOWN, LEFT, UP]

        prev_dir = 0

        while len(res) < n * m:
            dr, dc = spiral_directions[prev_dir]
            dn, dm = px + dr, py + dc
            if 0 <= dn < n and 0 <= dm < m and (dn, dm) not in visited:
                res.append(matrix[dn][dm])
                visited.add((dn, dm))
                px, py = dn, dm
            else:
                prev_dir = (prev_dir + 1) % len(spiral_directions)

        return res 

