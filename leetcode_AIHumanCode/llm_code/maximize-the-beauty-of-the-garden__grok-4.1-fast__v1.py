class Solution(object):
    def maximumBeauty(self, flowers):
        n = len(flowers)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (flowers[i] if flowers[i] > 0 else 0)
        first_occ = {}
        last_occ = {}
        for i, val in enumerate(flowers):
            if val not in first_occ:
                first_occ[val] = i
            last_occ[val] = i
        ans = float('-inf')
        for val in first_occ:
            if last_occ[val] > first_occ[val]:
                l_idx = first_occ[val]
                r_idx = last_occ[val]
                pos_sum = pref[r_idx + 1] - pref[l_idx]
                adjust = 2 * val if val < 0 else 0
                ans = max(ans, pos_sum + adjust)
        return ans
