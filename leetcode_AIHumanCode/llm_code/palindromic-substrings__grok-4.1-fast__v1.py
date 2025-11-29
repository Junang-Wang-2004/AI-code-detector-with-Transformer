class Solution:
    def countSubstrings(self, s):
        t = ['^']
        for ch in s:
            t.append('#')
            t.append(ch)
        t.append('#')
        t.append('$')
        n = len(t)
        radii = [0] * n
        center = 0
        boundary = 0
        for i in range(1, n - 1):
            mirror_pos = 2 * center - i
            if i < boundary:
                radii[i] = min(boundary - i, radii[mirror_pos])
            left = i - 1 - radii[i]
            right = i + 1 + radii[i]
            while left >= 0 and right < n and t[left] == t[right]:
                radii[i] += 1
                left -= 1
                right += 1
            if i + radii[i] > boundary:
                center = i
                boundary = i + radii[i]
        return sum((r + 1) // 2 for r in radii)
