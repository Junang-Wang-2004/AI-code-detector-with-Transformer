from functools import reduce

class C1(object):

    def discountPrices(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        while v2 < len(a1):
            v3 = a1.find(' ', v2)
            if v3 == -1:
                v3 = len(a1)
            if a1[v2] == '$' and v3 - (v2 + 1) > 0 and all((a1[k].isdigit() for v4 in range(v2 + 1, v3))):
                v5 = reduce(lambda x, y: x * 10 + int(y), (a1[v4] for v4 in range(v2 + 1, v3)), 0)
                v1.append('${:d}.{:02d}'.format(*divmod(v5 * (100 - a2), 100)))
            else:
                for v4 in range(v2, v3):
                    v1.append(a1[v4])
            if v3 != len(a1):
                v1.append(' ')
            v2 = v3 + 1
        return ''.join(v1)
