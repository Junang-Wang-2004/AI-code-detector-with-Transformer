import string
from functools import reduce

class C1(object):

    def twoEditWords(self, a1, a2):
        """
        """
        v1 = (1 << 64) - 59
        v2 = 113
        v3 = [1]

        def add(a1, a2):
            return (a1 + a2) % v1

        def mult(a1, a2):
            return a1 * a2 % v1

        def pow(a1):
            while not a1 < len(v3):
                v3.append(mult(v3[-1], v2))
            return v3[a1]
        v4 = set()
        for v5 in a2:
            v6 = reduce(lambda h, i: add(v6, mult(ord(v5[i]) - ord('a'), pow(i))), range(len(v5)), 0)
            for v7, v8 in enumerate(v5):
                for v9 in string.ascii_lowercase:
                    if v9 == v8:
                        continue
                    v4.add(add(v6, mult(ord(v9) - ord(v8), pow(v7))))
        v10 = []
        for v5 in a1:
            v6 = reduce(lambda h, i: add(v6, mult(ord(v5[v7]) - ord('a'), pow(v7))), range(len(v5)), 0)
            for v7, v8 in enumerate(v5):
                for v9 in string.ascii_lowercase:
                    if v9 == v8:
                        continue
                    if add(v6, mult(ord(v9) - ord(v8), pow(v7))) in v4:
                        break
                else:
                    continue
                v10.append(v5)
                break
        return v10
