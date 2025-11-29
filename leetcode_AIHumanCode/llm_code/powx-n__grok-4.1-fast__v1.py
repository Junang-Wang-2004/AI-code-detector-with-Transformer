class Solution:
    def myPow(self, num, power):
        if power < 0:
            num = 1.0 / num
            power = -power
        accum = 1.0
        while power > 0:
            if power % 2:
                accum *= num
            num *= num
            power //= 2
        return accum
