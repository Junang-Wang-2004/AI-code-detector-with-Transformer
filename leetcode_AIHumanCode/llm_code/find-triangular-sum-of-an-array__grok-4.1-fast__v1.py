class Solution:
    def triangularSum(self, nums):
        def strip_factor(x, p):
            if x == 0:
                return 0, 0
            val = 0
            while x % p == 0:
                x //= p
                val += 1
            return x, val

        def pow_2_mod10(e):
            cycle = [2, 4, 8, 6]
            return cycle[(e - 1) % 4]

        def pow_5_mod10(e):
            return 5

        def mod10_inv(last_digit):
            mapping = {1: 1, 3: 7, 7: 3, 9: 9}
            return mapping[last_digit]

        length = len(nums)
        answer = 0
        binom = 1
        val2 = 0
        val5 = 0
        for pos in range(length):
            if val2 == 0 and val5 == 0:
                multiplier = 1
            elif val2 > 0 and val5 == 0:
                multiplier = pow_2_mod10(val2)
            elif val2 == 0 and val5 > 0:
                multiplier = pow_5_mod10(val5)
            else:
                multiplier = 0
            term = (binom * multiplier) % 10
            answer = (answer + term * nums[pos]) % 10
            # prepare next binomial coefficient
            top, delta2 = strip_factor(length - 1 - pos, 2)
            val2 += delta2
            top, delta5 = strip_factor(top, 5)
            val5 += delta5
            bottom, delta2 = strip_factor(pos + 1, 2)
            val2 -= delta2
            bottom, delta5 = strip_factor(bottom, 5)
            val5 -= delta5
            binom = (binom * (top % 10)) % 10
            inv_bottom = mod10_inv(bottom % 10)
            binom = (binom * inv_bottom) % 10
        return answer
