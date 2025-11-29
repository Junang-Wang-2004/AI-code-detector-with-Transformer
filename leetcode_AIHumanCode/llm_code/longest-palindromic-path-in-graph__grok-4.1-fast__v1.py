class Solution(object):
    def maxLen(self, n, edges, label):
        complete_size = n * (n - 1) // 2
        if len(edges) == complete_size:
            freq = [0] * 26
            for ch in label:
                freq[ord(ch) - ord('a')] += 1
            paired = sum(2 * (f // 2) for f in freq)
            return paired + (1 if any(f % 2 != 0 for f in freq) else 0)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        states = [set() for _ in range(1 << n)]
        for i in range(n):
            bm = 1 << i
            states[bm].add((i, i))
        for x, y in edges:
            if label[x] == label[y]:
                bm = (1 << x) | (1 << y)
                lo, hi = min(x, y), max(x, y)
                states[bm].add((lo, hi))
        sizes = [bin(k).count('1') for k in range(1 << n)]
        maximum = 0
        for bm in range(1, 1 << n):
            if states[bm]:
                maximum = max(maximum, sizes[bm])
            for pr in states[bm]:
                p1, p2 = pr
                for nx in g[p1]:
                    if bm & (1 << nx):
                        continue
                    for ny in g[p2]:
                        if (bm & (1 << ny)) or nx == ny:
                            continue
                        if label[nx] == label[ny]:
                            nbm = bm | (1 << nx) | (1 << ny)
                            lo, hi = min(nx, ny), max(nx, ny)
                            states[nbm].add((lo, hi))
        return maximum
