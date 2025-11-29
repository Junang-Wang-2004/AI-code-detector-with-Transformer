class Solution:
    def popcountDepth(self, n, k):
        if k == 0:
            return 1
        if k == 1:
            return n.bit_length() - 1
        bits = []
        temp = n
        while temp:
            bits.append(temp % 2)
            temp //= 2
        bits.reverse()
        length = len(bits)
        depths = [0] * (length + 2)
        for num in range(2, length + 1):
            pc = 0
            val = num
            while val > 0:
                pc += val & 1
                val >>= 1
            depths[num] = 1 + depths[pc]
        dp = [[[0 for _ in range(2)] for _ in range(length + 1)] for _ in range(length + 1)]
        dp[0][0][1] = 1
        for pos in range(length):
            for ones_cnt in range(length + 1):
                for tight in range(2):
                    ways = dp[pos][ones_cnt][tight]
                    if ways == 0:
                        continue
                    upper = bits[pos] if tight == 1 else 1
                    for digit in range(2):
                        if digit > upper:
                            continue
                        new_tight = 1 if tight == 1 and digit == upper else 0
                        new_ones = ones_cnt + digit
                        if new_ones > length:
                            continue
                        dp[pos + 1][new_ones][new_tight] += ways
        total = 0
        for c in range(2, length + 1):
            if depths[c] == k - 1:
                total += dp[length][c][0] + dp[length][c][1]
        return total
