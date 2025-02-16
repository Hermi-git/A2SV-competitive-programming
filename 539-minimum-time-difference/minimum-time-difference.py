class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            total_minutes = hours * 60 + minutes
            return total_minutes 

        minute = sorted(time_to_minutes(timePoint) for timePoint in timePoints)
        
        n = len(timePoints)
        min_diff = float('inf')
        for i in range(n-1):  
            cur_diff =  minute[i + 1] - minute[i]
            min_diff = min(min_diff, cur_diff)
        circular_diff = (minute[0] + 1440) - minute[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff
        

