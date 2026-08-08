class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        output = [intervals[0]]
        
        for r in range(1,len(intervals)):
            pre_start, pre_end = output[-1]
            start, end = intervals[r]
            if pre_start <= start <= pre_end: # overlap
                if pre_end <= end:
                    output[-1] = [pre_start, end]
            else:
                output.append(intervals[r])
        return output







