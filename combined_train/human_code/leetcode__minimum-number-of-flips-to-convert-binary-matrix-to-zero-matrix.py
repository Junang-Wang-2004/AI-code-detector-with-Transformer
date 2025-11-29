import collections

class C1(object):

    def minFlips(self, a1):
        """
        """
        v1 = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = sum((val << r * len(a1[0]) + c for v3, v4 in enumerate(a1) for v5, v6 in enumerate(v4)))
        v7 = collections.deque([(v2, 0)])
        v8 = {v2}
        while v7:
            v9, v10 = v7.popleft()
            if not v9:
                return v10
            for v3 in range(len(a1)):
                for v5 in range(len(a1[0])):
                    v11 = v9
                    for v12, v13 in v1:
                        v14, v15 = (v3 + v12, v5 + v13)
                        if 0 <= v14 < len(a1) and 0 <= v15 < len(a1[0]):
                            v11 ^= 1 << v14 * len(a1[0]) + v15
                    if v11 in v8:
                        continue
                    v8.add(v11)
                    v7.append((v11, v10 + 1))
        return -1
