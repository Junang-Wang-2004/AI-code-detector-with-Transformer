class Solution:
    def gcdOfStrings(self, a, b):
        if not a or not b:
            return ""
        def find_gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        gc = find_gcd(len(a), len(b))
        if a + b == b + a:
            return a[:gc]
        return ""
