class C1:

    def intToRoman(self, a1):
        v1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        v2 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        v3 = []
        for v4, v5 in zip(v1, v2):
            while a1 >= v4:
                v3.append(v5)
                a1 -= v4
        return ''.join(v3)
