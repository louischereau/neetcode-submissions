import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for i, point in enumerate(points):
            distance = pow(pow(point[0], 2) + pow(point[1], 2), 0.5)
            distances.append((distance, i))
        
        heapq.heapify(distances)

        print(heapq.nsmallest(k, distances))

        return list(map(lambda x: points[x[1]], heapq.nsmallest(k, distances)))



        
        