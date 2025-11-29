# Time:  O(n^2 * k), n = len(str(high))
# Space: O(n * k)
# dp (slower but less space)
class Solution2(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        """
        TIGHT, UNTIGHT, UNBOUND = list(range(3))
        def f(x):
            digits = list(map(int, str(x)))
            dp = [[[0]*k for _ in range(2*len(digits)+1)] for _ in range(3)]
            for tight in range(2):
                for state in (TIGHT, UNTIGHT):
                    dp[state][0][0] = 1
            for i in reversed(range(len(digits))):
                new_dp = [[[0]*k for _ in range(2*len(digits)+1)] for _ in range(3)]
                for state in (TIGHT, UNTIGHT, UNBOUND):
                    new_dp[state][0][0] = int(i != 0)  # count if the beautiful integer x s.t. len(str(x)) < len(digits)
                    for d in range(1 if i == 0 else 0, 10):
                        new_state = state
                        if state == TIGHT and d != digits[i]:
                            new_state = UNTIGHT if d < digits[i] else UNBOUND
                        for diff in range(-len(digits), len(digits)+1):
                            new_diff = diff+(1 if d%2 == 0 else -1)
                            for total in range(k):
                                new_total = (total*10+d)%k
                                new_dp[state][diff][total] += dp[new_state][new_diff][new_total]
                dp = new_dp
            return dp[TIGHT][0][0]

        return f(high)-f(low-1)


