class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        minp = min(prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] for i in range(n))
        
        def feasible(tgt):
            st_copy = list(stations)
            remain = k
            right0 = min(n - 1, r)
            curr = sum(st_copy[:right0 + 1])
            for pos in range(n):
                if curr < tgt:
                    need = tgt - curr
                    if need > remain:
                        return False
                    remain -= need
                    curr += need
                    right_pos = min(n - 1, pos + r)
                    st_copy[right_pos] += need
                if pos == n - 1:
                    break
                old_left = max(0, pos - r)
                new_left = max(0, pos + 1 - r)
                old_right = min(n - 1, pos + r)
                new_right = min(n - 1, pos + 1 + r)
                if new_left > old_left:
                    curr -= st_copy[old_left]
                if new_right > old_right:
                    curr += st_copy[new_right]
            return True
        
        lo, hi = minp, minp + k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
