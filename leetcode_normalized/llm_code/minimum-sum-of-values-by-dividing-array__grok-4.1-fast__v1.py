import collections

class C1:

    def minimumValueSum(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        if v1 < v2:
            return -1
        v3 = 10 ** 20
        v4 = [v3] * (v1 + 1)
        v4[0] = 0
        v5 = max(a1).bit_length() if a1 else 0
        v5 = max(v5, 1)
        for v6 in range(v2):
            v7 = a2[v6]
            v8 = [v3] * (v1 + 1)
            v9 = [0] * v5
            v10 = v6
            v11 = v6
            v12 = [0] * (v1 + 1)
            v13 = collections.deque()
            for v14 in range(v6, v1):
                for v15 in range(v5):
                    if a1[v14] & 1 << v15:
                        v9[v15] += 1
                v16 = v14 - v10 + 1
                v17 = 0
                for v15 in range(v5):
                    if v9[v15] == v16:
                        v17 |= 1 << v15
                if v17 <= v7:
                    while v10 <= v14:
                        v18 = v14 - v10 + 1
                        v19 = 0
                        for v15 in range(v5):
                            if v9[v15] == v18:
                                v19 |= 1 << v15
                        if v19 > v7:
                            break
                        for v15 in range(v5):
                            if a1[v10] & 1 << v15:
                                v9[v15] -= 1
                        v10 += 1
                    v10 -= 1
                    for v15 in range(v5):
                        if a1[v10] & 1 << v15:
                            v9[v15] += 1
                v16 = v14 - v10 + 1
                v17 = 0
                for v15 in range(v5):
                    if v9[v15] == v16:
                        v17 |= 1 << v15
                v20 = v7 & a1[v14] == v7
                if v20:
                    v12[v14 + 1] = v12[v14] + 1
                else:
                    v12[v14 + 1] = 0
                if v17 == v7:
                    while v11 <= v10:
                        while v13 and v4[v13[-1]] >= v4[v11]:
                            v13.pop()
                        v13.append(v11)
                        v11 += 1
                    v21 = max(v6, v10 - v12[v10])
                    while v13 and v13[0] < v21:
                        v13.popleft()
                    if v13:
                        v8[v14 + 1] = min(v8[v14 + 1], v4[v13[0]] + a1[v14])
            v4 = v8
        return v4[v1] if v4[v1] < v3 else -1
