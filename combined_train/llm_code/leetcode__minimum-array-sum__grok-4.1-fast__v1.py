class C1(object):

    def minArraySum(self, a1, a2, a3, a4):
        a1.sort()
        v1 = len(a1)
        import bisect
        v2 = bisect.bisect_left(a1, a2)
        v3 = bisect.bisect_left(a1, 2 * a2 - 1)
        v4 = [False] * v1
        v5 = 0
        v6 = a3
        v7 = a4
        v8 = v1
        while v6 > 0 and v8 > v3:
            v8 -= 1
            v9 = a1[v8]
            a1[v8] = (v9 + 1) // 2
            v6 -= 1
            if v7 > 0:
                a1[v8] -= a2
                v7 -= 1
        v10 = v8 - 1
        v8 = v2
        while v7 > 0 and v8 <= v10:
            if a2 % 2 == 1 and a1[v8] % 2 == 0:
                v4[v8] = True
            a1[v8] -= a2
            v7 -= 1
            v8 += 1
        v11 = v8
        v8 = v10
        while v6 > 0 and v8 >= v11:
            v9 = a1[v8]
            a1[v8] = (v9 + 1) // 2
            v6 -= 1
            if a2 % 2 == 1 and v9 % 2 == 1:
                v5 += 1
            v8 -= 1
        v12 = sorted(((a1[i], i) for v13 in range(v11)))
        while v6 > 0 and v12:
            v9, v13 = v12.pop()
            a1[v13] = (v9 + 1) // 2
            if v5 > 0 and v4[v13]:
                v5 -= 1
                a1[v13] -= 1
            v6 -= 1
        return sum(a1)
