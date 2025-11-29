import collections

class C1:

    def kSimilarity(self, a1, a2):
        v1 = {}
        v2 = collections.deque([a1])
        v1[a1] = 0
        v3 = len(a1)
        while v2:
            v4 = v2.popleft()
            if v4 == a2:
                return v1[v4]
            v5 = list(v4)
            v6 = 0
            while v6 < v3 and v5[v6] == a2[v6]:
                v6 += 1
            v7 = a2[v6]
            for v8 in range(v6 + 1, v3):
                if v5[v8] == v7:
                    v5[v6], v5[v8] = (v5[v8], v5[v6])
                    v9 = ''.join(v5)
                    if v9 not in v1:
                        v1[v9] = v1[v4] + 1
                        v2.append(v9)
                    v5[v6], v5[v8] = (v5[v8], v5[v6])
