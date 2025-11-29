class C1:

    def smallestSubsequence(self, a1, a2, a3, a4):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1 - 1, -1, -1):
            v2[v3] = v2[v3 + 1] + (a1[v3] == a3)
        v4 = []
        v5 = a4
        for v6, v7 in enumerate(a1):
            while v4 and v4[-1] > v7 and (len(v4) + v1 - v6 > a2) and (v4[-1] != a3 or v5 + 1 <= v2[v6]):
                if v4.pop() == a3:
                    v5 += 1
            v8 = 1 if v7 == a3 else 0
            if len(v4) < a2 - (v5 - v8):
                if v8:
                    v5 -= 1
                v4.append(v7)
        return ''.join(v4)
