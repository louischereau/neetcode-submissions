from collections import deque

class ZigzagIterator:
    
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v for v in [v1, v2] if v]
        self.queue = deque(range(len(self.vectors)))
        self.indices = [0] * len(self.vectors)

    def next(self) -> int:
        vector_index = self.queue.popleft()
        vector = self.vectors[vector_index]
        index = self.indices[vector_index]
        self.indices[vector_index] += 1
        if index + 1 < len(vector): self.queue.append(vector_index)
        return vector[index]

    def hasNext(self) -> bool:
        return self.queue
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
