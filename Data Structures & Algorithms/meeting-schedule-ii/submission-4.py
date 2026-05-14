"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([meeting.start for meeting in intervals])
        end = sorted([meeting.end for meeting in intervals])

        print(start)
        print(end)
        merged_meetings = 0
        start_ptr = 0
        end_ptr = 0

        while end_ptr < len(end) and start_ptr < len(start):
            if end[end_ptr] > start[start_ptr]: start_ptr += 1
            else: 
                merged_meetings += 1
                # end.pop(end_ptr)
                # start.pop(start_ptr)
                start_ptr += 1
                end_ptr += 1
        
        return len(intervals) - merged_meetings
        