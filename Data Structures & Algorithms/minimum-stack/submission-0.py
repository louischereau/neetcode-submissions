import heapq

class MinStack:

    def __init__(self):
        self.storage = []
        # Stores the running minimum up to index i
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.storage.append(val)
        val = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)

    def pop(self) -> None:
        self.storage.pop()
        self.minimum.pop()
        
    def top(self) -> int:
        return self.storage[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
        
