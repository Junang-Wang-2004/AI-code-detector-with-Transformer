class Solution:
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        sz = r - l + 1
        trans = [[1 if i + j < sz - 1 else 0 for j in range(sz)] for i in range(sz)]

        def mul_mat(p, q):
            pr = len(p)
            pc = len(p[0])
            qr = len(q)
            qc = len(q[0])
            res = [[0] * qc for _ in range(pr)]
            for i in range(pr):
                for k in range(qc):
                    s = 0
                    for j in range(pc):
                        s = (s + p[i][j] * q[j][k]) % MOD
                    res[i][k] = s
            return res

        def pow_mat(base, ex):
            dim = len(base)
            ident = [[1 if x == y else 0 for y in range(dim)] for x in range(dim)]
            while ex > 0:
                if ex & 1:
                    ident = mul_mat(ident, base)
                base = mul_mat(base, base)
                ex >>= 1
            return ident

        init_vec = [[1] * sz]
        if n == 1:
            tot = sum(init_vec[0]) % MOD
        else:
            powered = pow_mat(trans, n - 1)
            fin_vec = mul_mat(init_vec, powered)
            tot = sum(fin_vec[0]) % MOD
        return (tot * 2) % MOD
