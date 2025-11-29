class C1(object):

    def boxDelivering(self, a1, a2, a3, a4):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        v3 = [0] * (v1 + 2)
        for v4 in range(v1):
            v2[v4 + 1] = v2[v4] + a1[v4][1]
            if v4 > 0 and a1[v4][0] != a1[v4 - 1][0]:
                v3[v4 + 1] = v3[v4] + 1
            else:
                v3[v4 + 1] = v3[v4]
        v3[v1 + 1] = v3[v1]
        v5 = [0] * (v1 + 1)
        from collections import deque
        v6 = deque()
        v6.append(0)
        v7 = 0
        for v4 in range(1, v1 + 1):
            while v7 < v4 and v2[v4] - v2[v7] > a4:
                v7 += 1
            v8 = max(v7, v4 - a3, 0)
            while v6 and v6[0] < v8:
                v6.popleft()
            if v6:
                v9 = v6[0]
                v10 = v5[v9] - v3[v9 + 1]
                v5[v4] = 2 + v3[v4] + v10
            v11 = v5[v4] - v3[v4 + 1]
            while v6 and v5[v6[-1]] - v3[v6[-1] + 1] >= v11:
                v6.pop()
            v6.append(v4)
        return v5[v1]
