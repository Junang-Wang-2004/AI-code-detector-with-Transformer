class Solution:
    def nextClosestTime(self, time):
        digits = set(time.replace(':', ''))
        cur_h, cur_m = map(int, time.split(':'))
        total = cur_h * 60 + cur_m
        ans = ""
        min_diff = float('inf')
        for th in digits:
            for uh in digits:
                hh = int(th + uh)
                if not 0 <= hh <= 23:
                    continue
                for tm in digits:
                    for um in digits:
                        mm = int(tm + um)
                        if not 0 <= mm <= 59:
                            continue
                        tmin = hh * 60 + mm
                        diff = tmin - total if tmin > total else 1440 - total + tmin
                        if diff < min_diff:
                            min_diff = diff
                            ans = f"{th}{uh}:{tm}{um}"
        return ans
