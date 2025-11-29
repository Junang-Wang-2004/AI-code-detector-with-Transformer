import collections

class C1(object):

    def minimumSemesters(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = [0] * a1
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v2[v4 - 1] += 1
        v5 = collections.deque([(1, i) for v6 in range(a1) if not v2[v6]])
        v7 = 0
        v8 = a1
        while v5:
            v9, v10 = v5.popleft()
            v8 -= 1
            v7 = v9
            for v11 in v1[v10]:
                v2[v11] -= 1
                if not v2[v11]:
                    v5.append((v9 + 1, v11))
        return v7 if v8 == 0 else -1
