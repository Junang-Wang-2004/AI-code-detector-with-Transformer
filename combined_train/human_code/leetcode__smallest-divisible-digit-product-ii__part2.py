class C1(object):

    def smallestNumber(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def find_candidates(a1, a2):
            v1 = []
            for v2 in reversed(range(2, 9 + 1)):
                while a1 % v2 == 0:
                    a1 //= v2
                    v1.append(v2)
                    if len(v1) > a2:
                        return []
                if a1 == 1:
                    v1.reverse()
                    return v1
            return []

        def format(a1, a2):
            v1 = [1] * a2
            v2 = len(v1) - len(a1)
            for v3 in a1:
                v1[v2] = v3
                v2 += 1
            return ''.join(map(str, v1))
        v1 = list(map(int, a1))
        v2 = find_candidates(a2, float('inf'))
        if a2 != 1 and (not v2):
            return '-1'
        v3 = next((v3 for v3 in range(len(v1)) if not v1[v3]), len(v1))
        for v4 in range(v3, len(v1)):
            v1[v4] = 1
        v5 = [1] * (len(v1) + 1)
        for v3 in range(len(v5) - 1):
            v5[v3 + 1] = v5[v3] * v1[v3] % a2
        if not v5[-1]:
            return ''.join(map(str, v1))
        for v3 in reversed(range(len(v1))):
            v6 = a2 // gcd(a2, v5[v3])
            for v7 in range(v1[v3] + 1, 9 + 1):
                v8 = v6 // gcd(v6, v7)
                v9 = find_candidates(v8, len(v1) - 1 - v3)
                if v8 != 1 and (not v9):
                    continue
                v1[v3] = v7
                return ''.join(map(str, v1[:v3 + 1])) + format(v9, len(v1) - 1 - v3)
        return format(v2, max(len(v1) + 1, len(v2)))
