class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        if len(intervals) == 1:
            return merged
        
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            m_start, m_end = merged.pop()
            if start > m_end:
                merged.append([m_start, m_end])
                merged.append(intervals[i])

            elif start <= m_end:
                merged.append([min(start,m_start),  max(end,m_end)])
            
        return merged


        