class Solution:
    def smallestValue(self, num):
        def factor_sum(val):
            res = 0
            while val % 2 == 0:
                res += 2
                val //= 2
            check = 3
            while check * check <= val:
                while val % check == 0:
                    res += check
                    val //= check
                check += 2
            if val > 1:
                res += val
            return res
        
        while True:
            next_val = factor_sum(num)
            if next_val == num:
                return num
            num = next_val
