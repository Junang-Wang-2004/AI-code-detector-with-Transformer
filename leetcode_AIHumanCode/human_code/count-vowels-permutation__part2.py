# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def countVowelPermutation(self, n):
        """
        """
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, i, o, u = (e+i+u) % MOD, (a+i) % MOD, (e+o) % MOD, i, (i+o) % MOD
        return (a+e+i+o+u) % MOD
