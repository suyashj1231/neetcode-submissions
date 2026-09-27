class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_start =intervals[0][0]
        curr_end =intervals[0][1]
        ans = [[curr_start, curr_end]]

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if curr_end >= start:
                curr_end = max(curr_end, end)
                ans[-1] = [curr_start, curr_end]
            else:
                ans.append([start, end])
                curr_start = start
                curr_end = end

        return ans



