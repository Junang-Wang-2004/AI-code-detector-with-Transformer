import collections

class C1(object):

    def primeSubarray(self, a1, a2):
        v1 = 50000
        v2 = [True] * (v1 + 1)
        v2[0] = v2[1] = False
        for v3 in range(2, int(v1 ** 0.5) + 1):
            if v2[v3]:
                for v4 in range(v3 * v3, v1 + 1, v3):
                    v2[v4] = False
        v5 = [v3 for v3, v6 in enumerate(a1) if v6 <= v1 and v2[v6]]
        v7 = len(v5)
        if v7 < 2:
            return 0
        v8 = [a1[v5[v3]] for v3 in range(v7)]
        v9 = collections.deque()
        v10 = collections.deque()
        v11 = 0
        v12 = 0
        for v4 in range(v7):
            while v9 and v8[v9[-1]] <= v8[v4]:
                v9.pop()
            v9.append(v4)
            while v10 and v8[v10[-1]] >= v8[v4]:
                v10.pop()
            v10.append(v4)
            while v8[v9[0]] - v8[v10[0]] > a2:
                if v9 and v9[0] == v12:
                    v9.popleft()
                if v10 and v10[0] == v12:
                    v10.popleft()
                v12 += 1
            if v4 - v12 + 1 >= 2:
                v13 = v5[v4 - 1]
                v14 = 0 if v12 == 0 else v5[v12 - 1] + 1
                v11 += v13 - v14 + 1
        return v11
