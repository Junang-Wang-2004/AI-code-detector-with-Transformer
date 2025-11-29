class C1:

    def smallestSubsequence(self, a1):
        v1 = len(a1)
        v2 = {}
        for v3 in range(v1):
            v2[a1[v3]] = v3
        v4 = []
        v5 = set()
        for v6 in range(v1):
            v7 = a1[v6]
            if v7 not in v5:
                while v4 and v4[-1] > v7 and (v2[v4[-1]] > v6):
                    v5.remove(v4.pop())
                v4.append(v7)
                v5.add(v7)
        return ''.join(v4)
