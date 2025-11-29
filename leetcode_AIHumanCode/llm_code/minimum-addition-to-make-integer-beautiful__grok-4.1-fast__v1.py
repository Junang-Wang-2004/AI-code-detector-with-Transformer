class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        total = 0
        temp = n
        while temp > 0:
            total += temp % 10
            temp //= 10
        if total <= target:
            return 0
        added = 0
        current = n
        while total > target:
            power = 10
            while (current // power) % 10 == 9:
                power *= 10
            mod_val = current % power
            mod_sum = 0
            tmp = mod_val
            while tmp > 0:
                mod_sum += tmp % 10
                tmp //= 10
            total += 1 - mod_sum
            to_add = power - mod_val
            added += to_add
            current += to_add
        return added
