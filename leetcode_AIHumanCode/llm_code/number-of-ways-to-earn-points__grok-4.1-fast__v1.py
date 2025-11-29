class Solution(object):
    def waysToReachTarget(self, target, types):
        MOD = 10**9 + 7
        ways = [0] * (target + 1)
        ways[0] = 1
        for max_cnt, val in types:
            nxt = [0] * (target + 1)
            for cnt in range(max_cnt + 1):
                shift_amt = cnt * val
                for idx in range(target - shift_amt + 1):
                    nxt[idx + shift_amt] = (nxt[idx + shift_amt] + ways[idx]) % MOD
            ways = nxt
        return ways[target]
