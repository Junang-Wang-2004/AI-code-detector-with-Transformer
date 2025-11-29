import collections

class C1:

    def killProcess(self, a1, a2, a3):
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a2):
            v1[v3].append(a1[v2])
        v4 = []
        v5 = collections.deque([a3])
        while v5:
            v6 = v5.popleft()
            v4.append(v6)
            for v7 in v1[v6]:
                v5.append(v7)
        return v4
