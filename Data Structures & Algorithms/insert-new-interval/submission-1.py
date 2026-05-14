class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        startNew, endNew = newInterval

        for i, interval in enumerate(intervals):
            start, end = interval
            if end < startNew:
                res.append([start, end])
            elif start > endNew:
                res.append([startNew, endNew])
                return res + intervals[i:]
            else:
                startNew, endNew = min(startNew, start), max(endNew, end)
        res.append([startNew, endNew])
        return res