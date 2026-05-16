class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        # possible cases:
        # 1. new interval is in front, then also return everything after adding
        # 2. new interval is behind, but we need to check for oth intervals
        # 3. we had a interval so we also change newInterval to merged one
        # --> if none of these trigger basically interval is at end so we need it manually
        for index in range(len(intervals)):
            #. 1
            if intervals[index][0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[index:]
            
            # 2.
            elif intervals[index][1] < newInterval[0]:
                ans.append(intervals[index])

            # 3. merge 
            else:
                newInterval = [min(intervals[index][0], newInterval[0]), max(intervals[index][1], newInterval[1])]

        #4. at end
        ans.append(newInterval)
        return ans


        