import collections
from functools import reduce

class C1(object):

    def minimumValueSum(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = max(a1).bit_length()

        def update(a1, a2, a3):
            for v1 in range(v2):
                if a2 & 1 << v1:
                    a1[v1] += a3

        def mask(a1, a2):
            return reduce(lambda accu, i: accu | 1 << i, (i for v1 in range(v2) if a1[v1] == a2), 0)
        v3 = [v1] * (len(a1) + 1)
        v3[0] = 0
        for v4 in range(len(a2)):
            v5 = [v1] * (len(a1) + 1)
            v6 = [0] * v2
            v7 = [0] * len(v3)
            v8 = collections.deque()
            v9 = v10 = v4
            for v11 in range(v4, len(a1)):
                update(v6, a1[v11], +1)
                if mask(v6, v11 - v9 + 1) <= a2[v4]:
                    while v9 <= v11:
                        if mask(v6, v11 - v9 + 1) > a2[v4]:
                            break
                        update(v6, a1[v9], -1)
                        v9 += 1
                    v9 -= 1
                    update(v6, a1[v9], +1)
                if a2[v4] & a1[v11] == a2[v4]:
                    v7[v11 + 1] = v7[v11] + 1
                if mask(v6, v11 - v9 + 1) != a2[v4]:
                    continue
                while v10 <= v9:
                    while v8 and v3[v8[-1]] >= v3[v10]:
                        v8.pop()
                    v8.append(v10)
                    v10 += 1
                while v8 and v8[0] < v9 - v7[v9]:
                    v8.popleft()
                if v8:
                    v5[v11 + 1] = v3[v8[0]] + a1[v11]
            v3 = v5
        return v3[-1] if v3[-1] != v1 else -1
