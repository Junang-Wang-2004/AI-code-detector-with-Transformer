class Solution(object):
    def maxFreeTime(self, event_time, start_times, end_times):
        ext_starts = start_times + [event_time]
        ext_ends = [0] + end_times
        num_gaps = len(ext_starts)
        gaps = [ext_starts[j] - ext_ends[j] for j in range(num_gaps)]

        g1 = g2 = g3 = float('-inf')
        i1 = i2 = i3 = -1
        for j in range(num_gaps):
            g = gaps[j]
            if g > g1:
                g3, i3 = g2, i2
                g2, i2 = g1, i1
                g1, i1 = g, j
            elif g > g2:
                g3, i3 = g2, i2
                g2, i2 = g, j
            elif g > g3:
                g3, i3 = g, j

        top_gaps_idxs = [(g1, i1), (g2, i2), (g3, i3)]

        result = 0
        for pos in range(num_gaps - 1):
            gap_a = gaps[pos]
            gap_b = gaps[pos + 1]
            pair_sum = gap_a + gap_b
            event_dur = ext_ends[pos + 1] - ext_starts[pos]
            allow_skip = any(
                idx != pos and idx != pos + 1 and event_dur <= tg
                for tg, idx in top_gaps_idxs
            )
            candidate = pair_sum + event_dur if allow_skip else pair_sum
            if candidate > result:
                result = candidate
        return result
