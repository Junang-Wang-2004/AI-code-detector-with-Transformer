from collections import deque

class C1:

    def minimumOperations(self, a1, a2, a3):
        if a2 == a3:
            return 0
        v1 = 1000
        v2 = [-1] * (v1 + 1)
        v2[a2] = 0
        v3 = deque([a2])
        v4 = list({num for v5 in a1 if v5})
        while v3:
            v6 = v3.popleft()
            v7 = v2[v6]
            for v5 in v4:
                v8 = [v6 + v5, v6 - v5, v6 ^ v5]
                for v9 in v8:
                    if 0 <= v9 <= v1 and v2[v9] == -1:
                        v2[v9] = v7 + 1
                        if v9 == a3:
                            return v7 + 1
                        v3.append(v9)
        return -1
