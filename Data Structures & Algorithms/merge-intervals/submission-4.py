class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        if len(intervals) == 1:
            return intervals

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        results = [sorted_intervals[0]]

        ptr_left = -1 
        ptr_right = 1

        while ptr_right < len(intervals):
            if results[ptr_left][1] >= sorted_intervals[ptr_right][0]:
                interval = [results[ptr_left][0], max(results[ptr_left][1], sorted_intervals[ptr_right][1])]
                results[-1] = interval
                ptr_right += 1
            else:
                results.append(sorted_intervals[ptr_right])
                ptr_right += 1
        return results
