class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        results = [sorted_intervals[0]]

        ptr_left = 0
        ptr_right = ptr_left + 1

        while ptr_right < len(intervals):
            if results[ptr_left][1] >= sorted_intervals[ptr_right][0]:
                if results[ptr_left][1] < sorted_intervals[ptr_right][1]:
                    interval = [results[ptr_left][0], sorted_intervals[ptr_right][1]]
                else:
                    interval = results[ptr_left]
                results[-1] = interval
                ptr_right += 1
            else:
                results.append(sorted_intervals[ptr_right])
                ptr_left += 1
                ptr_right += 1
        return results
