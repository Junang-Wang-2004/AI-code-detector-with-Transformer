class Solution(object):
    def largestTimeFromDigits(self, digits):
        max_time = ""
        for p in range(4):
            for q in range(4):
                if q == p: continue
                for r in range(4):
                    if r == p or r == q: continue
                    s = 6 - (p + q + r)
                    hh = 10 * digits[p] + digits[q]
                    mm = 10 * digits[r] + digits[s]
                    if hh <= 23 and mm <= 59:
                        candidate = f"{hh:02d}:{mm:02d}"
                        if candidate > max_time:
                            max_time = candidate
        return max_time
