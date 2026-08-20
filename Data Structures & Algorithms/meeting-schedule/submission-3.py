"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x:x.start)
        if len(intervals) <= 1: return True
        init_end = intervals[0].end

        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if start < init_end: return False
            else:
                init_end = end
        return True
