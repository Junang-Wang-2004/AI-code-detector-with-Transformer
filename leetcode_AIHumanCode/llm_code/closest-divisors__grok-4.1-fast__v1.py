class Solution(object):
    def closestDivisors(self, num):
        a, b = num + 1, num + 2
        rt = int(b ** 0.5)
        for i in range(rt, 0, -1):
            if a % i == 0:
                return [i, a // i]
            if b % i == 0:
                return [i, b // i]
