from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        groups = defaultdict(list)
        n = len(nums)
        for idx, val in enumerate(nums):
            groups[val].append(idx)
        answer = [0] * n
        for positions in groups.values():
            m = len(positions)
            if m < 2:
                continue
            pref = [0] * (m + 1)
            for j in range(m):
                pref[j + 1] = pref[j] + positions[j]
            for k in range(m):
                lcnt = k
                lsum = pref[k]
                left = lcnt * positions[k] - lsum
                rcnt = m - k - 1
                rsum = pref[m] - pref[k + 1]
                right = rsum - rcnt * positions[k]
                answer[positions[k]] = left + right
        return answer
