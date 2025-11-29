class Solution:
    def eraseOverlapIntervals(self, intervals):
        sorted_ints = sorted(intervals, key=lambda x: x[1])
        kept = 0
        prev_end = float('-inf')
        for start, end in sorted_ints:
            if start >= prev_end:
                kept += 1
                prev_end = end
        return len(intervals) - kept
