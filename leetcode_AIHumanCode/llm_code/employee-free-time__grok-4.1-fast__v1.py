class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule):
        all_intervals = []
        for worker_shifts in schedule:
            for shift in worker_shifts:
                all_intervals.append((shift.start, shift.end))
        if not all_intervals:
            return []
        all_intervals.sort(key=lambda x: x[0])
        merged_busy = []
        curr_begin, curr_finish = all_intervals[0]
        for begin, finish in all_intervals[1:]:
            if begin <= curr_finish:
                curr_finish = max(curr_finish, finish)
            else:
                merged_busy.append(Interval(curr_begin, curr_finish))
                curr_begin, curr_finish = begin, finish
        merged_busy.append(Interval(curr_begin, curr_finish))
        free_periods = []
        for k in range(1, len(merged_busy)):
            gap_start = merged_busy[k - 1].end
            gap_end = merged_busy[k].start
            free_periods.append(Interval(gap_start, gap_end))
        return free_periods
