class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        is_diff = [0] * n
        for i in range(n):
            is_diff[i] = 1 if colors[i] != colors[(i + 1) % n] else 0
        doubled = is_diff + is_diff
        prefix = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix[i + 1] = prefix[i] + doubled[i]
        count = 0
        window_size = k - 1
        for start in range(n):
            if prefix[start + window_size] - prefix[start] == window_size:
                count += 1
        return count
