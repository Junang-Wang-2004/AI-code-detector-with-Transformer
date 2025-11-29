import collections

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(2 * v1 - 1):
            v5 = collections.defaultdict(int)
            v6 = 1
            v7, v8 = (v4 // 2, (v4 + 1) // 2)
            while 0 <= v7 and v8 < v1:
                for v9 in range(2):
                    v10, v11 = (a1[v7], a2[v8])
                    if v10 != v11 and (v7 != v8 or v9 == 0):
                        if v5[v11, v10]:
                            v5[v11, v10] -= 1
                        else:
                            v5[v10, v11] += 1
                            v6 += 1
                    v8, v7 = (v7, v8)
                v2[v7][v8] = v6
                v7 -= 1
                v8 += 1
        v12 = [float('inf')] * (v1 + 1)
        v12[0] = 0
        for v4 in range(v1):
            v5 = collections.defaultdict(int)
            v6 = 0
            for v9 in reversed(range(v4 + 1)):
                v10, v11 = (a1[v9], a2[v9])
                if v10 != v11:
                    if v5[v11, v10]:
                        v5[v11, v10] -= 1
                    else:
                        v5[v10, v11] += 1
                        v6 += 1
                v12[v4 + 1] = min(v12[v4 + 1], v12[v9] + min(v6, v2[v9][v4]))
        return v12[v1]
