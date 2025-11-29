class C1(object):

    def intToRoman(self, a1):
        """
        """
        v1 = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        v2, v3 = (sorted(v1.keys()), [])
        while a1 > 0:
            for v4 in reversed(v2):
                while a1 / v4 > 0:
                    a1 -= v4
                    v3 += v1[v4]
        return ''.join(v3)
