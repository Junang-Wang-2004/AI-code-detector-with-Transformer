class Solution(object):
    def countSubstrings(self, s, t):
        def diag(start_s, start_t):
            rem_s = len(s) - start_s
            rem_t = len(t) - start_t
            diag_len = min(rem_s, rem_t)
            mismatch_offsets = []
            for pos in range(diag_len):
                if s[start_s + pos] != t[start_t + pos]:
                    mismatch_offsets.append(pos)
            total = 0
            last_mis = -1
            num_mis = len(mismatch_offsets)
            for idx in range(num_mis):
                this_mis = mismatch_offsets[idx]
                starts_possible = this_mis - last_mis
                next_mis_pos = diag_len if idx + 1 == num_mis else mismatch_offsets[idx + 1]
                ends_possible = next_mis_pos - this_mis
                total += starts_possible * ends_possible
                last_mis = this_mis
            return total

        result = 0
        m = len(s)
        for begin_s in range(m):
            result += diag(begin_s, 0)
        n = len(t)
        for begin_t in range(1, n):
            result += diag(0, begin_t)
        return result
