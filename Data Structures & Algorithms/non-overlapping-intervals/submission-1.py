class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if prev_end > start:
                removals += 1
            else:
                prev_end = intervals[i][1]

        return removals
        