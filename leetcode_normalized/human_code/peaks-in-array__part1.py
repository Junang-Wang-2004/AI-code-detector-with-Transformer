class C1(object):

    def countOfPeaks(self, a1, a2):
        """
        """

        class BIT(object):

            def __init__(self, a1):
                self.__bit = [0] * (len(a1) + 1)
                for v1 in range(1, len(self.__bit)):
                    self.__bit[v1] = a1[v1 - 1] + self.__bit[v1 - 1]
                for v1 in reversed(range(1, len(self.__bit))):
                    v2 = v1 - (v1 & -v1)
                    self.__bit[v1] -= self.__bit[v2]

            def add(self, a1, a2):
                a1 += 1
                while a1 < len(self.__bit):
                    self.__bit[a1] += a2
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 += self.__bit[a1]
                    a1 -= a1 & -a1
                return v2

        def check(a1):
            return a1[a1 - 1] < a1[a1] > a1[a1 + 1]

        def update(a1, a2):
            for v1 in range(max(a1 - 1, 1), min(a1 + 1 + 1, len(a1) - 1)):
                if check(v1):
                    bit.add(v1, a2)
        v1 = BIT([int(1 <= i <= len(a1) - 2 and check(i)) for v2 in range(len(a1))])
        v3 = []
        for v4, v5, v6 in a2:
            if v4 == 1:
                v3.append(v1.query(v6 - 1) - v1.query(v5 + 1 - 1) if v6 - 1 >= v5 + 1 else 0)
                continue
            update(v5, -1)
            a1[v5] = v6
            update(v5, +1)
        return v3
