# Time:  O((r - l)^3 * logn)
# Space: O((r - l)^2)

import itertools
from functools import reduce


# matrix fast exponentiation
class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        """
        MOD = 10**9+7
        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b % MOD for a, b in zip(row, col)) % MOD for col in ZB] for row in A]
 
        def matrix_expo(A, K):
            result = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result
    
        r -= l
        matrix = [[int(i+j < r) for j in range(r+1)] for i in range(r+1)]
        matrix_pow_t = matrix_expo(matrix, n-1)
        return (reduce(lambda accu, x: (accu+x)%MOD, matrix_mult([[1]*(r+1)], matrix_pow_t)[0], 0)*2)%MOD
