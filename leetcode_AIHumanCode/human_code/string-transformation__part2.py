from functools import reduce
# Time:  O(n + logk)
# Space: O(n)
# dp, matrix exponentiation, kmp
class Solution2(object):
    def numberOfWays(self, s, t, k):
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

        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern):
            prefix = getPrefix(pattern)
            j = -1
            for i in range(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    yield i-j
                    j = prefix[j]

        n = len(s)
        T = [[0, 1],
             [n-1, (n-1)-1]]
        dp = [1, 0]
        dp = matrix_mult([dp], matrix_expo(T, k))[0]  # [dp[0], dp[1]] * T^k
        return reduce(lambda a, b: (a+b)%MOD, (dp[int(i != 0)] for i in KMP(s+s[:-1], t)), 0)


