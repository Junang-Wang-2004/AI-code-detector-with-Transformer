class Solution:
    def longestCommonSubpath(self, n, paths):
        def substr_hashes(seq, length):
            size = len(seq)
            if length > size:
                return set()
            hash1 = [0] * (size + 1)
            pow1 = [1] * (size + 1)
            hash2 = [0] * (size + 1)
            pow2 = [1] * (size + 1)
            b1, b2 = 131, 137
            m1, m2 = 1000000007, 1000000009
            for j in range(1, size + 1):
                hash1[j] = (hash1[j - 1] * b1 + seq[j - 1]) % m1
                pow1[j] = pow1[j - 1] * b1 % m1
                hash2[j] = (hash2[j - 1] * b2 + seq[j - 1]) % m2
                pow2[j] = pow2[j - 1] * b2 % m2
            res = set()
            for start in range(length, size + 1):
                h1 = (hash1[start] - hash1[start - length] * pow1[length] % m1 + m1) % m1
                h2 = (hash2[start] - hash2[start - length] * pow2[length] % m2 + m2) % m2
                res.add((h1, h2))
            return res

        def feasible(length):
            if length == 0:
                return True
            common = substr_hashes(paths[0], length)
            for seq in paths[1:]:
                common &= substr_hashes(seq, length)
                if not common:
                    return False
            return bool(common)

        max_possible = min(len(p) for p in paths)
        low, high = 0, max_possible
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
