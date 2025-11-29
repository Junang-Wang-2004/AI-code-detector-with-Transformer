import itertools

class C1(object):

    def maxProfit(self, a1, a2):
        """
        """
        v1 = float('-inf')

        class BIT(object):

            def __init__(self, a1, a2=0, a3=lambda x, y: x + y):
                self.__bit = [v1] * (a1 + 1)
                self.__default = a2
                self.__fn = a3

            def update(self, a1, a2):
                a1 += 1
                while a1 < len(self.__bit):
                    self.__bit[a1] = self.__fn(self.__bit[a1], a2)
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = self.__default
                while a1 > 0:
                    v2 = self.__fn(v2, self.__bit[a1])
                    a1 -= a1 & -a1
                return v2
        v2 = {x: i for v3, v4 in enumerate(sorted(set(a1)))}
        v5 = v1
        v6, v7 = (BIT(len(v2), default=v1, fn=max), BIT(len(v2), default=v1, fn=max))
        for v8, v9 in zip(a1, a2):
            v5 = max(v5, v7.query(v2[v8] - 1) + v9)
            v6.update(v2[v8], v9)
            v7.update(v2[v8], v6.query(v2[v8] - 1) + v9)
        return v5 if v5 != v1 else -1
