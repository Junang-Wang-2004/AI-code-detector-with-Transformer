class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        if n == 0:
            return 0
        MOD = 10**9 + 7
        first_occur = [[-1] * 4 for _ in range(n)]
        last_occur = [[-1] * 4 for _ in range(n)]
        for c in range(4):
            ptr = -1
            for i in range(n - 1, -1, -1):
                if ord(S[i]) - ord('a') == c:
                    ptr = i
                first_occur[i][c] = ptr
            ptr = -1
            for i in range(n):
                if ord(S[i]) - ord('a') == c:
                    ptr = i
                last_occur[i][c] = ptr
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for begin in range(n - length + 1):
                fin = begin + length - 1
                total = 1
                for c in range(4):
                    left_pos = first_occur[begin][c]
                    if left_pos == -1 or left_pos > fin:
                        continue
                    total = (total + 1) % MOD
                    right_pos = last_occur[fin][c]
                    if left_pos < right_pos:
                        in_l = left_pos + 1
                        in_r = right_pos - 1
                        if in_l > in_r:
                            total = (total + 1) % MOD
                        else:
                            total = (total + dp[in_l][in_r]) % MOD
                dp[begin][fin] = total
        return (dp[0][n - 1] - 1 + MOD) % MOD
