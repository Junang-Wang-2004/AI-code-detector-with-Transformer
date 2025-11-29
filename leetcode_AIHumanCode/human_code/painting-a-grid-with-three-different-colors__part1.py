# Time:  O(m * 2^m + 3^m + 2^(3 * m) * logn) = O(2^(3 * m) * logn)
# Space: O(2^(2 * m))

import collections
import itertools
from functools import reduce


# better complexity for small m, super large n
# matrix exponentiation solution
class Solution(object):
    def colorTheGrid(self, m, n):
        """
        """
        MOD = 10**9+7
        def backtracking(mask1, mask2, basis, result):  # Time: O(2^m), Space: O(2^m)
            if not basis:
                result.append(mask2)
                return
            for i in range(3):
                if (mask1 == -1 or mask1//basis%3 != i) and (mask2 == -1 or mask2//(basis*3)%3 != i):
                    backtracking(mask1, mask2+i*basis if mask2 != -1 else i*basis, basis//3, result)

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

        def normalize(basis, mask):
            norm = {}
            result = 0
            while basis:
                x = mask//basis%3
                if x not in norm:
                    norm[x] = len(norm)
                result += norm[x]*basis
                basis //= 3
            return result

        if m > n:
            m, n = n, m
        basis = 3**(m-1)
        masks = []
        backtracking(-1, -1, basis, masks)  # Time: O(2^m), Space: O(2^m)
        assert(len(masks) == 3 * 2**(m-1))
        lookup = {mask:normalize(basis, mask) for mask in masks}  # Time: O(m * 2^m)
        normalized_mask_cnt = collections.Counter(lookup[mask] for mask in masks)
        assert(len(normalized_mask_cnt) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
        adj = collections.defaultdict(list)
        for mask in normalized_mask_cnt.keys():  # O(3^m) leaves which are all in depth m => Time: O(3^m), Space: O(3^m)
            backtracking(mask, -1, basis, adj[mask])
        normalized_adj = collections.defaultdict(lambda:collections.defaultdict(int))
        for mask1, masks2 in adj.items():
            for mask2 in masks2:
                normalized_adj[mask1][lookup[mask2]] = (normalized_adj[mask1][lookup[mask2]]+1)%MOD
        # divided by 3 * 2 is since the first two colors in upper row are normalized to speed up performance,
        # since first two colors in lower row which has at most 3 choices could be also normalized, lower bound is upper bound divided by at most 3
        assert(2*3**m // 3 // 2 // 3 <= sum(len(v) for v in normalized_adj.values()) <= 2*3**m // 3 // 2)
        return reduce(lambda x,y: (x+y)%MOD,
                      matrix_mult([list(normalized_mask_cnt.values())],
                                   matrix_expo([[normalized_adj[mask1][mask2]
                                                 for mask2 in normalized_mask_cnt.keys()] 
                                                 for mask1 in normalized_mask_cnt.keys()], n-1))[0],
                      0)  # Time: O((2^m)^3 * logn), Space: O((2^m)^2)


