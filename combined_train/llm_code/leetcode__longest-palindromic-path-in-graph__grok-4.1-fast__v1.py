class C1(object):

    def maxLen(self, a1, a2, a3):
        v1 = a1 * (a1 - 1) // 2
        if len(a2) == v1:
            v2 = [0] * 26
            for v3 in a3:
                v2[ord(v3) - ord('a')] += 1
            v4 = sum((2 * (f // 2) for v5 in v2))
            return v4 + (1 if any((v5 % 2 != 0 for v5 in v2)) else 0)
        v6 = [[] for v7 in range(a1)]
        for v8, v9 in a2:
            v6[v8].append(v9)
            v6[v9].append(v8)
        v10 = [set() for v7 in range(1 << a1)]
        for v11 in range(a1):
            v12 = 1 << v11
            v10[v12].add((v11, v11))
        for v8, v9 in a2:
            if a3[v8] == a3[v9]:
                v12 = 1 << v8 | 1 << v9
                v13, v14 = (min(v8, v9), max(v8, v9))
                v10[v12].add((v13, v14))
        v15 = [bin(k).count('1') for v16 in range(1 << a1)]
        v17 = 0
        for v12 in range(1, 1 << a1):
            if v10[v12]:
                v17 = max(v17, v15[v12])
            for v18 in v10[v12]:
                v19, v20 = v18
                for v21 in v6[v19]:
                    if v12 & 1 << v21:
                        continue
                    for v22 in v6[v20]:
                        if v12 & 1 << v22 or v21 == v22:
                            continue
                        if a3[v21] == a3[v22]:
                            v23 = v12 | 1 << v21 | 1 << v22
                            v13, v14 = (min(v21, v22), max(v21, v22))
                            v10[v23].add((v13, v14))
        return v17
