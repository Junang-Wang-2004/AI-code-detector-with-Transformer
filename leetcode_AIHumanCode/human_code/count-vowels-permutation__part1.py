# Time:  O(logn)
# Space: O(1)

import itertools


class Solution(object):
    def countVowelPermutation(self, n):
        """
        """
        def matrix_expo(A, K):
            result = [[int(i==j) for j in range(len(A))] \
                      for i in range(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b for a, b in zip(row, col)) % MOD \
                     for col in ZB] for row in A]
        
        MOD = 10**9 + 7
        T = [[0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 1, 0]]
        return sum(map(sum, matrix_expo(T, n-1))) % MOD


