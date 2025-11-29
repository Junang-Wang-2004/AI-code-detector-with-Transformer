class Solution:
    def canMakePalindromeQueries(self, s: str, queries):
        n = len(s)
        half = n // 2
        A = ord('a')
        mismatch_cum = [0] * (half + 1)
        lfreq = [[0] * 26 for _ in range(half + 1)]
        rfreq = [[0] * 26 for _ in range(half + 1)]
        for i in range(half):
            cl = ord(s[i]) - A
            cr = ord(s[n - 1 - i]) - A
            mismatch_cum[i + 1] = mismatch_cum[i] + (1 if cl != cr else 0)
            lfreq[i + 1] = lfreq[i][:]
            lfreq[i + 1][cl] += 1
            rfreq[i + 1] = rfreq[i][:]
            rfreq[i + 1][cr] += 1

        def get_segment_freq(pre, start, end):
            return [pre[end + 1][j] - pre[start][j] for j in range(26)]

        def multisets_equal(start, end):
            return get_segment_freq(lfreq, start, end) == get_segment_freq(rfreq, start, end)

        def is_possible(left1, right1, left2, right2):
            min_start = min(left1, left2)
            max_end = max(right1, right2)
            min_end = min(right1, right2)
            max_start = max(left1, left2)
            if mismatch_cum[min_start] != 0 or mismatch_cum[half] - mismatch_cum[max_end + 1] != 0:
                return False
            if min_end < max_start:
                if mismatch_cum[max_start] - mismatch_cum[min_end + 1] != 0:
                    return False
                return multisets_equal(min_start, min_end) and multisets_equal(max_start, max_end)
            contains = (left1 == min_start) == (right1 == max_end)
            if contains:
                return multisets_equal(min_start, max_end)
            l_pre, r_pre = (lfreq, rfreq) if left1 == min_start else (rfreq, lfreq)
            seg1_l = get_segment_freq(l_pre, min_start, min_end)
            seg1_r = [r_pre[max_start][j] - r_pre[min_start][j] for j in range(26)]
            diff1 = [seg1_l[j] - seg1_r[j] for j in range(26)]
            seg2_r = get_segment_freq(r_pre, max_start, max_end)
            seg2_l = get_segment_freq(l_pre, min_end + 1, max_end)
            diff2 = [seg2_r[j] - seg2_l[j] for j in range(26)]
            return diff1 == diff2 and all(x >= 0 for x in diff1)

        return [is_possible(q[0], q[1], n - 1 - q[3], n - 1 - q[2]) for q in queries]
