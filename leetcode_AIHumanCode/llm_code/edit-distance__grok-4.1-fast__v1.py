class Solution:
    def minDistance(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        n = len(a)
        m = len(b)
        previous = list(range(m + 1))
        for x in range(1, n + 1):
            current = [x] * (m + 1)
            for y in range(1, m + 1):
                add = current[y - 1] + 1
                remove = previous[y] + 1
                subst = previous[y - 1] + (1 if a[x - 1] != b[y - 1] else 0)
                current[y] = min(add, remove, subst)
            previous = current
        return previous[m]
