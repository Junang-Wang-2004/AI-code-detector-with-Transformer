# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfWays(self, num_people):
        """
        """
        MOD = 10**9+7
        def inv(x, m):  # Euler's Theorem
            return pow(x, m-2, m)  # O(logMOD) = O(1)

        def nCr(n, k, m):
            if n-k < k:
                return nCr(n, n-k, m)
            result = 1
            for i in range(1, k+1):
                result = result*(n-k+i)*inv(i, m)%m
            return result

        n = num_people//2
        return nCr(2*n, n, MOD)*inv(n+1, MOD) % MOD  # Catalan number


