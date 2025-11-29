import collections

class Solution:
    def threeSumMulti(self, A, target):
        freq = collections.Counter(A)
        keys = list(freq)
        res = 0
        MOD = 10**9 + 7
        n = len(keys)
        for i in range(n):
            for j in range(i, n):
                x = keys[i]
                y = keys[j]
                z = target - x - y
                if z not in freq:
                    continue
                cx = freq[x]
                cy = freq[y]
                cz = freq[z]
                if x == y == z:
                    res += cx * (cx - 1) * (cx - 2) // 6
                elif x == y:
                    res += cx * (cx - 1) // 2 * cz
                elif max(x, y) < z:
                    res += cx * cy * cz
        return res % MOD
