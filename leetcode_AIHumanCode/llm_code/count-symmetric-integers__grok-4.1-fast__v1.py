class Solution:
    def countSymmetricIntegers(self, low, high):
        def is_symmetric(n):
            s = str(n)
            l = len(s)
            if l % 2 != 0:
                return False
            m = l // 2
            left_sum = sum(int(c) for c in s[:m])
            right_sum = sum(int(c) for c in s[m:])
            return left_sum == right_sum

        total = 0
        for val in range(low, high + 1):
            if is_symmetric(val):
                total += 1
        return total
