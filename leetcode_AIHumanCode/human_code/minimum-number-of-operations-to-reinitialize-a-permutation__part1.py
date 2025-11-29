# Time:  O(sqrt(n))
# Space: O(sqrt(n))

class Solution(object):
    def reinitializePermutation(self, n):
        """
        """
        # reference: https://cp-algorithms.com/algebra/discrete-log.html
        def discrete_log(a, b, m):
            a %= m
            b %= m
            n = int(m**0.5)+1
            an = pow(a, n, m)
            vals = {}
            curr = b
            for q in range(n+1):
                vals[curr] = q
                curr = curr*a % m
            curr = 1
            for p in range(1, n+1):
                curr = curr*an % m
                if curr in vals:
                    return n*p-vals[curr]
            return -1

        return 1+discrete_log(2, n//2, n-1)  # find min x s.t. 2^x mod (n-1) = n/2, result is x + 1


