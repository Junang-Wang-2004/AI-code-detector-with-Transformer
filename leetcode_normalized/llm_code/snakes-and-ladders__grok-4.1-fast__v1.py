import collections

class C1:

    def snakesAndLadders(self, a1):
        v1 = len(a1)
        v2 = v1 * v1
        v3 = [-1] * (v2 + 1)
        v3[1] = 0
        v4 = collections.deque([1])
        while v4:
            v5 = v4.popleft()
            for v6 in range(1, 7):
                v7 = v5 + v6
                if v7 > v2:
                    break
                v8 = (v7 - 1) // v1
                v9 = v1 - 1 - v8
                v10 = (v7 - 1) % v1
                if v8 % 2 == 1:
                    v10 = v1 - 1 - v10
                v11 = a1[v9][v10] if a1[v9][v10] != -1 else v7
                if v3[v11] == -1:
                    v3[v11] = v3[v5] + 1
                    v4.append(v11)
                    if v11 == v2:
                        return v3[v2]
        return -1
