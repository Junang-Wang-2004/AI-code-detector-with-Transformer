from collections import deque

class C1:

    def minimumTotalPrice(self, a1, a2, a3, a4):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        for v6, v7 in a4:
            if v6 == v7:
                v5[v6] += 1
                continue
            v8 = [-1] * a1
            v9 = deque([v6])
            v8[v6] = -2
            v10 = False
            while v9 and (not v10):
                v11 = v9.popleft()
                for v12 in v1[v11]:
                    if v8[v12] == -1:
                        v8[v12] = v11
                        v9.append(v12)
                        if v12 == v7:
                            v10 = True
                            break
            v11 = v7
            while v11 != v6:
                v5[v11] += 1
                v11 = v8[v11]
            v5[v6] += 1

        def tree_dp(a1, a2):
            v1 = a3[a1] * v5[a1]
            v2 = a3[a1] // 2 * v5[a1]
            for v3 in v1[a1]:
                if v3 == a2:
                    continue
                v4, v5 = tree_dp(v3, a1)
                v1 += min(v4, v5)
                v2 += v4
            return (v1, v2)
        v13, v14 = tree_dp(0, -1)
        return min(v13, v14)
