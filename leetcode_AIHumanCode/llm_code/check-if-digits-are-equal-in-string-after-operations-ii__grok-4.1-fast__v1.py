class Solution:
    def hasSameDigits(self, s):
        length = len(s)
        if length < 2:
            return True
        mm = length - 2
        def small_c(n_val, r_val, prime):
            if r_val > n_val:
                return 0
            if r_val > n_val - r_val:
                r_val = n_val - r_val
            prod = 1
            for j in range(1, r_val + 1):
                prod = prod * (n_val - j + 1) // j
            return prod % prime

        def lucas_theorem(na, ka, pa):
            if ka < 0 or ka > na:
                return 0
            prod_l = 1
            na_temp = na
            ka_temp = ka
            while na_temp > 0 or ka_temp > 0:
                n_digit = na_temp % pa
                k_digit = ka_temp % pa
                if k_digit > n_digit:
                    return 0
                prod_l = (prod_l * small_c(n_digit, k_digit, pa)) % pa
                na_temp //= pa
                ka_temp //= pa
            return prod_l

        def coeff_mod10(na, ka):
            mod2_val = lucas_theorem(na, ka, 2)
            mod5_val = lucas_theorem(na, ka, 5)
            for candidate in range(10):
                if candidate % 2 == mod2_val and candidate % 5 == mod5_val:
                    return candidate
            return 0

        running_sum = 0
        for ii in range(mm + 1):
            weight = coeff_mod10(mm, ii)
            delta_val = ord(s[ii]) - ord(s[ii + 1])
            running_sum = (running_sum + weight * delta_val) % 10
        return running_sum == 0
