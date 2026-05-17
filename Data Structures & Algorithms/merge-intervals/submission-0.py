class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        initStart = intervals[0][0]
        initEnd = intervals[0][1]
        merged = []
        for start, end in intervals[1:]:
            if start <= initEnd: # overlap
                initEnd = max(end, initEnd)
            
            else:
                merged.append([initStart, initEnd])
                initStart = start
                initEnd = end
        merged.append([initStart, initEnd])
        return merged



