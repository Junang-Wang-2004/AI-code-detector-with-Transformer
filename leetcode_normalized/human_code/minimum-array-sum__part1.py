class C1(object):

    def minArraySum(self, a1, a2, a3, a4):
        """
        """
        a1.sort()
        v1 = next((i for v2 in range(len(a1)) if a1[v2] >= a2), len(a1))
        v3 = next((v2 for v2 in range(len(a1)) if a1[v2] >= 2 * a2 - 1), len(a1))
        v4, v5 = ([False] * len(a1), 0)
        for v6 in reversed(range(v3, len(a1))):
            if not a3:
                break
            a3 -= 1
            a1[v6] = (a1[v6] + 1) // 2
            if a4:
                a4 -= 1
                a1[v6] -= a2
        else:
            v6 = v3 - 1
        for v2 in range(v1, v6 + 1):
            if not a4:
                break
            a4 -= 1
            if a2 % 2 == 1 and a1[v2] % 2 == 0:
                v4[v2] = True
            a1[v2] -= a2
        else:
            v2 = v6 + 1
        for v6 in reversed(range(v2, v6 + 1)):
            if not a3:
                break
            a3 -= 1
            if a2 % 2 == 1 and a1[v6] % 2 == 1:
                v5 += 1
            a1[v6] = (a1[v6] + 1) // 2
        else:
            v6 = v2 - 1
        v9 = sorted(((a1[idx], idx) for v10 in range(v2)))
        for v11 in range(a3):
            v12, v10 = v9.pop()
            a1[v10] = (v12 + 1) // 2
            if v5 and v4[v10]:
                v5 -= 1
                a1[v10] -= 1
        return sum(a1)
