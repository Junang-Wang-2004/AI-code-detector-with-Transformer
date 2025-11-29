from collections import Counter

class Solution:
    def numberOfPairs(self, lista, listb, factor):
        if not lista:
            return 0
        maxnum = max(lista) + 1
        divisors = [0] * maxnum
        freq = Counter(listb)
        for y, qty in freq.items():
            prod = factor * y
            pos = prod
            while pos < maxnum:
                divisors[pos] += qty
                pos += prod
        return sum(divisors[val] for val in lista)
