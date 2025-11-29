class Solution:
    def captureForts(self, forts):
        ans = 0
        prev_idx = -1
        prev_sign = 0
        for idx in range(len(forts)):
            if forts[idx] != 0:
                if prev_idx >= 0 and forts[idx] == -prev_sign:
                    ans = max(ans, idx - prev_idx - 1)
                prev_idx = idx
                prev_sign = forts[idx]
        return ans
