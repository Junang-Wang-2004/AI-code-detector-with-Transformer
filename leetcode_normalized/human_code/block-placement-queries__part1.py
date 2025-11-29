from sortedcontainers import SortedList

class C1(object):

    def getResults(self, a1):
        """
        """

        class BIT(object):

            def __init__(self, a1, a2=0, a3=lambda x, y: x + y):
                self.__bit = [a2] * (a1 + 1)
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
        v1 = SortedList((q[1] for v2 in a1 if v2[0] == 1))
        v3 = {x: i for v4, v5 in enumerate(v1)}
        v6 = BIT(len(v3), fn=max)
        for v4 in range(len(v1)):
            v6.update(v3[v1[v4]], v1[v4] - (v1[v4 - 1] if v4 - 1 >= 0 else 0))
        v7 = []
        for v2 in reversed(a1):
            v4 = v1.bisect_left(v2[1])
            if v2[0] == 1:
                if v4 + 1 < len(v1):
                    v6.update(v3[v1[v4 + 1]], v1[v4 + 1] - (v1[v4 - 1] if v4 - 1 >= 0 else 0))
                del v1[v4]
            else:
                v7.append(v2[1] - (v1[v4 - 1] if v4 - 1 >= 0 else 0) >= v2[2] or (v4 - 1 >= 0 and v6.query(v3[v1[v4 - 1]]) >= v2[2]))
        v7.reverse()
        return v7
