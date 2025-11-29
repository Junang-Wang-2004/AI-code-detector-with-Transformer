class Solution:
    def digitsCount(self, d, low, high):
        def count_upto(num):
            if num < 0:
                return 0
            res = 0
            factor = 1
            while factor <= num:
                res += (num // (factor * 10)) * factor
                rem = num % (factor * 10)
                if rem >= d * factor:
                    res += min(factor, rem - d * factor + 1)
                if d == 0:
                    res -= factor
                factor *= 10
            return res + 1
        
        return count_upto(high) - count_upto(low - 1)
