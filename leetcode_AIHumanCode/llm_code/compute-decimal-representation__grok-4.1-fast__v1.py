class Solution:
    def decimalRepresentation(self, n):
        terms = []
        if n == 0:
            return terms
        place = 1
        while place * 10 <= n:
            place *= 10
        while n > 0:
            d = n // place
            if d:
                terms.append(d * place)
            n %= place
            place //= 10
        return terms
