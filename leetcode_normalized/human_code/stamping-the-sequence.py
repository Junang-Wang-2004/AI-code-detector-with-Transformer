import collections

class C1(object):

    def movesToStamp(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = collections.deque()
        v4 = [False] * v2
        v5 = []
        v6 = []
        for v7 in range(v2 - v1 + 1):
            v8, v9 = (set(), set())
            for v10, v11 in enumerate(a1):
                if v11 == a2[v7 + v10]:
                    v8.add(v7 + v10)
                else:
                    v9.add(v7 + v10)
            v6.append((v8, v9))
            if v9:
                continue
            v5.append(v7)
            for v12 in v8:
                if v4[v12]:
                    continue
                v3.append(v12)
                v4[v12] = True
        while v3:
            v7 = v3.popleft()
            for v10 in range(max(0, v7 - v1 + 1), min(v2 - v1, v7) + 1):
                v8, v9 = v6[v10]
                if v7 not in v9:
                    continue
                v9.discard(v7)
                if v9:
                    continue
                v5.append(v10)
                for v12 in v8:
                    if v4[v12]:
                        continue
                    v3.append(v12)
                    v4[v12] = True
        return v5[::-1] if all(v4) else []
