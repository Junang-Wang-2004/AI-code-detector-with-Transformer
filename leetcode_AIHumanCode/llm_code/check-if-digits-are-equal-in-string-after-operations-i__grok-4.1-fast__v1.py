class Solution:
    def hasSameDigits(self, s):
        length = len(s)
        if length < 2:
            return True
        vals = [int(c) for c in s]
        deltas = [vals[j] - vals[j + 1] for j in range(length - 1)]
        mm = length - 2

        def sum_mod_prime(pr):
            accum = 0
            for idx in range(mm + 1):
                bc = lucas(mm, idx, pr)
                accum = (accum + bc * (deltas[idx] % pr)) % pr
            return accum

        def lucas(big_n, big_k, pr):
            if big_k < 0 or big_k > big_n:
                return 0
            prod = 1
            while big_n or big_k:
                nd = big_n % pr
                kd = big_k % pr
                if kd > nd:
                    return 0
                prod = (prod * small_binom(nd, kd)) % pr
                big_n //= pr
                big_k //= pr
            return prod

        def small_binom(aa, bb):
            if bb > aa - bb:
                bb = aa - bb
            if bb == 0:
                return 1
            res = 1
            for t in range(1, bb + 1):
                res *= (aa - t + 1)
                res //= t
            return res

        return sum_mod_prime(2) == 0 and sum_mod_prime(5) == 0
