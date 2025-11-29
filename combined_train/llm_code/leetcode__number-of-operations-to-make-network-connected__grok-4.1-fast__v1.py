from collections import defaultdict, deque

class C1:

    def makeConnected(self, a1, a2):
        if len(a2) < a1 - 1:
            return -1
        v1 = defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = set()
        v5 = 0
        for v6 in range(a1):
            if v6 not in v4:
                v5 += 1
                v7 = deque([v6])
                v4.add(v6)
                while v7:
                    v8 = v7.popleft()
                    for v9 in v1[v8]:
                        if v9 not in v4:
                            v4.add(v9)
                            v7.append(v9)
        return v5 - 1
