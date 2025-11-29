class Solution:
    def numTilings(self, n):
        MOD = 10**9 + 7
        
        def multiply(A, B):
            rows_A = len(A)
            cols_B = len(B[0])
            cols_A = len(A[0])
            C = [[0] * cols_B for _ in range(rows_A)]
            for i in range(rows_A):
                for j in range(cols_B):
                    for k in range(cols_A):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        
        def power(base, exponent):
            size = len(base)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while exponent > 0:
                if exponent % 2 == 1:
                    result = multiply(result, base)
                base = multiply(base, base)
                exponent //= 2
            return result
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        trans = [[2, 0, 1], [1, 0, 0], [0, 1, 0]]
        vec = [[2], [1], [1]]
        powered = power(trans, n - 2)
        final = multiply(powered, vec)
        return final[0][0]
