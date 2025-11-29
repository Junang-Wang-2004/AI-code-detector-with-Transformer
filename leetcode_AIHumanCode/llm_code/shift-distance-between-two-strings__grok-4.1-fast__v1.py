class Solution:
    def shiftDistance(self, s, t, nextCost, previousCost):
        def build_prefix(costs):
            pref = [0]
            for val in costs:
                pref.append(pref[-1] + val)
            return pref

        next_pref = build_prefix(nextCost)
        prev_pref = build_prefix(previousCost)
        tot_next = next_pref[-1]
        tot_prev = prev_pref[-1]

        def next_shift(fr, to):
            if fr <= to:
                return next_pref[to] - next_pref[fr]
            return tot_next + next_pref[to] - next_pref[fr]

        def prev_shift(fr, to):
            if fr >= to:
                return prev_pref[fr + 1] - prev_pref[to + 1]
            return tot_prev - (prev_pref[to + 1] - prev_pref[fr + 1])

        total = 0
        for char_s, char_t in zip(s, t):
            if char_s == char_t:
                continue
            idx_s = ord(char_s) - ord('a')
            idx_t = ord(char_t) - ord('a')
            total += min(next_shift(idx_s, idx_t), prev_shift(idx_s, idx_t))
        return total
