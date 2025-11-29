class Solution:
    def minimumTimeToInitialState(self, s, m):
        n = len(s)
        prefix_match = [0] * n
        left_box = 0
        right_box = 0
        for j in range(1, n):
            if j <= right_box:
                prefix_match[j] = min(right_box - j + 1, prefix_match[j - left_box])
            while j + prefix_match[j] < n and s[prefix_match[j]] == s[j + prefix_match[j]]:
                prefix_match[j] += 1
            if j + prefix_match[j] - 1 > right_box:
                left_box = j
                right_box = j + prefix_match[j] - 1
        turns = 1
        while turns * m < n:
            position = turns * m
            suffix_len = n - position
            if prefix_match[position] >= suffix_len:
                return turns
            turns += 1
        return turns
