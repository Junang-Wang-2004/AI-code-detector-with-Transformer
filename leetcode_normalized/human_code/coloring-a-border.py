import collections

class C1(object):

    def colorBorder(self, a1, a2, a3, a4):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        v2, v3, v4 = (set([(a2, a3)]), collections.deque([(a2, a3)]), [])
        while v3:
            v5, v6 = v3.popleft()
            v7 = False
            for v8 in v1:
                v9, v10 = (v5 + v8[0], v6 + v8[1])
                if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (a1[v9][v10] == a1[v5][v6])):
                    v7 = True
                    continue
                if (v9, v10) in v2:
                    continue
                v2.add((v9, v10))
                v3.append((v9, v10))
            if v7:
                v4.append((v5, v6))
        for v5, v6 in v4:
            a1[v5][v6] = a4
        return a1
