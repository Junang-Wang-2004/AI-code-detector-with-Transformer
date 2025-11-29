class C1(object):

    def closestFair(self, a1):
        """
        """
        v1 = list(map(int, str(a1)))
        v2 = []
        if len(v1) % 2 == 0:
            v3 = [0] * 2
            for v4 in v1:
                v3[v4 % 2] += 1
            if v3[0] == len(v1) // 2:
                return a1
            for v5 in reversed(range(len(v1) // 2, len(v1))):
                v3[v1[v5] % 2] -= 1
                v6 = [len(v1) // 2 - v3[0], len(v1) // 2 - v3[1]]
                if any((x < 0 for v7 in v6)):
                    continue
                v4 = v1[v5] + 1 if v6[(v1[v5] + 1) % 2] - 1 >= 0 else v1[v5] + 2
                if v4 > 9:
                    continue
                v6[v4 % 2] -= 1
                v2 = v1[:v5] + [v4] + [0] * v6[0] + [1] * v6[1]
                break
        if not v2:
            v8 = len(v1) // 2 + 1
            v2 = [1] + [0] * v8 + [1] * (v8 - 1)
        return int(''.join(map(str, v2)))
