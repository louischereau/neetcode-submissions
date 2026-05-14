class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key, 0):
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:

        if not self.store.get(key, 0):
            return ""

        values = self.store[key]

        lo, hi = 0, len(values) - 1

        while lo <= hi:
            middle = (lo + hi) // 2

            mid_value, mid_timestamp = values[middle]

            if mid_timestamp > timestamp: 
                hi = middle - 1
            else: 
                lo = middle + 1

        return values[hi][0] if hi >= 0 else ""
        
