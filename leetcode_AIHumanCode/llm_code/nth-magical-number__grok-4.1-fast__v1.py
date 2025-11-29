class Solution:
    def nthMagicalNumber(self, n, a, b):
        def get_gcd(x, y):
            return x if y == 0 else get_gcd(y, x % y)
        lcm_val = a * b // get_gcd(a, b)
        def count_divisible_by_a_or_b(val):
            return val // a + val // b - val // lcm_val
        low, high = 1, 10**18
        while low < high:
            middle = (low + high) // 2
            if count_divisible_by_a_or_b(middle) >= n:
                high = middle
            else:
                low = middle + 1
        return low % (10**9 + 7)
