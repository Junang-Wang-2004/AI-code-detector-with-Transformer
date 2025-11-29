class Solution:
    def countStableSubarrays(self, nums, queries):
        n = len(nums)
        seg_start = []
        seg_end = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j] <= nums[j + 1]:
                j += 1
            seg_start.append(i)
            seg_end.append(j)
            i = j + 1
        num_seg = len(seg_start)
        contrib = [0] * num_seg
        pref_cont = [0] * (num_seg + 1)
        for k in range(num_seg):
            ln = seg_end[k] - seg_start[k] + 1
            contrib[k] = ln * (ln + 1) // 2
            pref_cont[k + 1] = pref_cont[k] + contrib[k]
        seg_idx = [-1] * n
        for k in range(num_seg):
            for p in range(seg_start[k], seg_end[k] + 1):
                seg_idx[p] = k
        result = []
        for L, R in queries:
            sL = seg_idx[L]
            sR = seg_idx[R]
            if sL == sR:
                le = R - L + 1
                tot = le * (le + 1) // 2
            else:
                eL = seg_end[sL]
                leL = eL - L + 1
                cL = leL * (leL + 1) // 2
                sRt = seg_start[sR]
                leR = R - sRt + 1
                cR = leR * (leR + 1) // 2
                cM = pref_cont[sR] - pref_cont[sL + 1]
                tot = cL + cM + cR
            result.append(tot)
        return result
