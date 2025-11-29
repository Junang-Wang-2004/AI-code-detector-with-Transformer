class Solution:
    def minimumTime(self, s):
        n = len(s)
        prefix_ones = 0
        ans = float('inf')
        total_ones = 0
        for c in s:
            total_ones += (c == '1')
        cur_ones = 0
        for i in range(n + 1):
            left_c = min(i, 2 * cur_ones)
            right_c = min(n - i, 2 * (total_ones - cur_ones))
            ans = min(ans, left_c + right_c)
            if i < n:
                cur_ones += (s[i] == '1')
        return ans
