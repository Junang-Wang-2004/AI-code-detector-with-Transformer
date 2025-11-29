from functools import reduce
# Time:  O(p^3 * logh), p is the number of patterns, p may be up to 512
# Space: O(p^3)
# bitmask, backtracking, matrix exponentiation
class Solution_TLE(object):
    def buildWall(self, height, width, bricks):
        """
        """
        MOD = 10**9+7
        def backtracking(height, width, bricks, total, mask, lookup, patterns):
            if mask in lookup:
                return
            lookup.add(mask)
            if total >= width:
                if total == width:
                    patterns.append(mask^(1<<width))
                return
            for x in bricks:
                backtracking(height, width, bricks, total+x, mask|(1<<(total+x)), lookup, patterns)

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

        patterns, lookup = [], set()
        backtracking(height, width, bricks, 0, 0, lookup, patterns)
        return reduce(lambda x,y: (x+y)%MOD,
                      matrix_mult([[1]*len(patterns)],
                                   matrix_expo([[int((mask1 & mask2) == 0)
                                                 for mask2 in patterns] 
                                                 for mask1 in patterns], height-1))[0],
                      0)  # Time: O(p^3 * logh), Space: O(p^2)
