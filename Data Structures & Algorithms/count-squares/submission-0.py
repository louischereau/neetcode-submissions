class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        if self.points.get(tuple(point)):
            self.points[tuple(point)] += 1
        else:
            self.points[tuple(point)] = 1
        

    def count(self, point: List[int]) -> int:
        count = 0

        for (px, py), p_count in self.points.items():
            dx, dy = abs(px - point[0]), abs(py - point[1])
            if dx == dy and dx != 0:
                corner1_count = self.points.get((px, point[1]), 0)
                corner2_count = self.points.get((point[0], py), 0)
                count += corner1_count * corner2_count * p_count
    
        return count


        
