class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        vals = sorted(f for f in freq if f > 0)
        m = len(vals)
        prefix = [0]
        for v in vals:
            prefix.append(prefix[-1] + v)
        res = n
        j = 0
        for i in range(m):
            target = vals[i]
            while j < m and vals[j] <= target + k:
                j += 1
            del_left = prefix[i]
            high_sum = prefix[m] - prefix[j]
            high_cnt = m - j
            del_right = high_sum - (target + k) * high_cnt
            res = min(res, del_left + del_right)
        return res
