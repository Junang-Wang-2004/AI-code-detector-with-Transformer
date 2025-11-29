# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n * k)
# dp (slower but less space)
class Solution4(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        """
        def f(x):
            digits = list(map(int, str(x)))
            dp = [[[[0]*k for _ in range(2*len(digits)+1)] for _ in range(2)] for _ in range(2)]
            for tight in range(2):
                dp[0][tight][0][0] = 1
            for i in reversed(range(len(digits))):
                new_dp = [[[[0]*k for _ in range(2*len(digits)+1)] for _ in range(2)] for _ in range(2)]
                for zero in range(2):
                    for tight in range(2):
                        for d in range((digits[i] if tight else 9)+1):
                            new_zero = int(zero and d == 0)
                            new_tight = int(tight and d == digits[i])
                            for diff in range(-len(digits), len(digits)+1):
                                new_diff = diff+((1 if d%2 == 0 else -1) if new_zero == 0 else 0)
                                for total in range(k):
                                    new_total = (total*10+d)%k
                                    new_dp[zero][tight][diff][total] += dp[new_zero][new_tight][new_diff][new_total]
                dp = new_dp
            return dp[1][1][0][0]

        return f(high)-f(low-1)
