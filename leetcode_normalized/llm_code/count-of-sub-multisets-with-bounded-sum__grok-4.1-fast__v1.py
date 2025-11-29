import collections

class C1(object):

    def countSubMultisets(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = collections.Counter(a1)
        v3 = v2.pop(0, 0)
        v4 = [0] * (a3 + 1)
        v4[0] = 1
        for v5, v6 in v2.items():
            for v7 in range(v5):
                v8 = [0]
                v9 = v7
                while v9 <= a3:
                    v8.append((v8[-1] + v4[v9]) % v1)
                    v9 += v5
                v9 = v7
                v10 = 0
                while v9 <= a3:
                    v11 = max(0, v10 - v6)
                    v4[v9] = (v8[v10 + 1] - v8[v11] + v1) % v1
                    v9 += v5
                    v10 += 1
        v12 = sum((v4[v10] for v10 in range(a2, a3 + 1))) % v1
        return v12 * (v3 + 1) % v1
