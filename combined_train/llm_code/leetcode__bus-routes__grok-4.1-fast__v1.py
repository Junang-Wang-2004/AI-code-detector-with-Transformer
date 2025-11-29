from collections import deque, defaultdict

class C1:

    def numBusesToDestination(self, a1, a2, a3):
        if a2 == a3:
            return 0
        v1 = defaultdict(list)
        for v2, v3 in enumerate(a1):
            for v4 in v3:
                v1[v4].append(v2)
        v5 = deque([a2])
        v6 = {a2}
        v7 = set()
        v8 = 0
        while v5:
            v9 = len(v5)
            for v10 in range(v9):
                v11 = v5.popleft()
                for v2 in v1[v11]:
                    if v2 in v7:
                        continue
                    v7.add(v2)
                    for v12 in a1[v2]:
                        if v12 not in v6:
                            if v12 == a3:
                                return v8 + 1
                            v6.add(v12)
                            v5.append(v12)
            v8 += 1
        return -1
