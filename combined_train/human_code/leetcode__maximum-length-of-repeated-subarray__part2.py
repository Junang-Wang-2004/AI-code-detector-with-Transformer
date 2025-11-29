class C1(object):

    def findLength(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            return self.findLength(a2, a1)
        v1, v2 = (10 ** 9 + 7, 113)
        v3 = pow(v2, v1 - 2, v1)

        def check(a1):

            def rolling_hashes(a1, a2):
                if a2 == 0:
                    yield (0, 0)
                    return
                v1, v2 = (0, 1)
                for v3, v4 in enumerate(a1):
                    v1 = (v1 + v4 * v2) % v1
                    if v3 < a2 - 1:
                        v2 = v2 * v2 % v1
                    else:
                        yield (v1, v3 - (a2 - 1))
                        v1 = (v1 - a1[v3 - (a2 - 1)]) * v3 % v1
            v1 = collections.defaultdict(list)
            for v2, v3 in rolling_hashes(a1, a1):
                v1[v2].append(v3)
            for v2, v4 in rolling_hashes(a2, a1):
                if any((a1[v3:v3 + a1] == a2[v4:v4 + a1] for v3 in v1[v2])):
                    return True
            return False
        v4, v5 = (0, min(len(a1), len(a2)) + 1)
        while v4 < v5:
            v6 = v4 + (v5 - v4) / 2
            if not check(v6):
                v5 = v6
            else:
                v4 = v6 + 1
        return v4 - 1
