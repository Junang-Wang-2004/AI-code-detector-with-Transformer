class Solution:
    def numberOfWays(self, n, m, k, source, dest):
        MOD = 10**9 + 7
        SIZE = 4

        def multiply(A, B):
            result = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                for j in range(SIZE):
                    for p in range(SIZE):
                        result[i][j] = (result[i][j] + A[i][p] * B[p][j]) % MOD
            return result

        def power(mat, exp):
            res = [[1 if i == j else 0 for j in range(SIZE)] for i in range(SIZE)]
            while exp > 0:
                if exp & 1:
                    res = multiply(res, mat)
                mat = multiply(mat, mat)
                exp >>= 1
            return res

        trans = [
            [0, m - 1, n - 1, 0],
            [1, m - 2, 0, n - 1],
            [1, 0, n - 2, m - 1],
            [0, 1, 1, n + m - 4]
        ]

        powered = power(trans, k)

        sr, sc = source
        dr, dc = dest
        if sr == dr and sc == dc:
            vec = [1, 0, 0, 0]
        elif sr == dr:
            vec = [0, 1, 0, 0]
        elif sc == dc:
            vec = [0, 0, 1, 0]
        else:
            vec = [0, 0, 0, 1]

        ans = 0
        for i in range(SIZE):
            ans = (ans + vec[i] * powered[i][0]) % MOD
        return ans
