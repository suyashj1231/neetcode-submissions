"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        curr = 0
        maxroom = 0
        s = e = 0

        while s < len(start):
  
            if start[s] < end[e]:
                curr +=1
                s+=1
            else:
                curr-=1
                e+=1
            maxroom = max(maxroom, curr)
        
        return maxroom

        