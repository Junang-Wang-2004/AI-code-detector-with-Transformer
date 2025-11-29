class Solution:
    def atMostNGivenDigitSet(self, D, N):
        s = str(N)
        length = len(s)
        base = len(D)
        allowed = set(D)
        shorter_count = 0
        pow_val = 1
        for _ in range(length - 1):
            pow_val *= base
            shorter_count += pow_val
        ans = shorter_count
        rem_digits = length
        tight = True
        for idx in range(length):
            curr_digit = s[idx]
            smaller_count = 0
            for dig in D:
                if dig < curr_digit:
                    smaller_count += 1
            ans += smaller_count * (base ** (rem_digits - 1))
            if curr_digit not in allowed:
                tight = False
                break
            rem_digits -= 1
        if tight:
            ans += 1
        return ans
