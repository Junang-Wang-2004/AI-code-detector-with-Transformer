from sortedcontainers import SortedList

class C1(object):

    def numberOfAlternatingGroups(self, a1, a2):
        """
        """

        class BIT(object):

            def __init__(self, a1):
                self.__bit = [0] * (a1 + 1)

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

        def update(a1, a2):
            if a2 == +1:
                sl.add(a1)
                if len(sl) == 1:
                    bit1.add(n, +1)
                    bit2.add(n, +n)
            v1 = sl.index(a1)
            v2, v3 = ((v1 - 1) % len(sl), (v1 + 1) % len(sl))
            if len(sl) != 1:
                v4 = (sl[v3] - sl[v2] - 1) % n + 1
                bit1.add(v4, a2 * -1)
                bit2.add(v4, a2 * -v4)
                v4 = (sl[v1] - sl[v2]) % n
                bit1.add(v4, a2 * +1)
                bit2.add(v4, a2 * +v4)
                v4 = (sl[v3] - sl[v1]) % n
                bit1.add(v4, a2 * +1)
                bit2.add(v4, a2 * +v4)
            if a2 == -1:
                if len(sl) == 1:
                    bit1.add(n, -1)
                    bit2.add(n, -n)
                sl.pop(v1)
        v1 = len(a1)
        v2 = SortedList()
        v3, v4 = (BIT(v1 + 1), BIT(v1 + 1))
        for v5 in range(v1):
            if a1[v5] == a1[(v5 + 1) % v1]:
                update(v5, +1)
        v6 = []
        for v7 in a2:
            if v7[0] == 1:
                v8 = v7[1]
                v6.append(v4.query(v1) - v4.query(v8 - 1) - (v8 - 1) * (v3.query(v1) - v3.query(v8 - 1)) if v2 else v1)
                continue
            v9, v5, v10 = v7
            if a1[v5] == v10:
                continue
            a1[v5] = v10
            update((v5 - 1) % v1, +1 if a1[v5] == a1[(v5 - 1) % v1] else -1)
            update(v5, +1 if a1[v5] == a1[(v5 + 1) % v1] else -1)
        return v6
