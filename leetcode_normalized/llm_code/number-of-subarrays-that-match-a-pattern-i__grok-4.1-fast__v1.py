class C1:

    def countMatchingSubarrays(self, a1, a2):
        v1 = len(a1)
        if v1 == 0 or not a2:
            return 0
        v2 = []
        for v3 in range(v1 - 1):
            if a1[v3 + 1] > a1[v3]:
                v2.append(1)
            elif a1[v3 + 1] < a1[v3]:
                v2.append(-1)
            else:
                v2.append(0)

        def longest_prefix_suffix(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = 0
            v4 = 1
            while v4 < v1:
                if a1[v4] == a1[v3]:
                    v3 += 1
                    v2[v4] = v3
                    v4 += 1
                elif v3 > 0:
                    v3 = v2[v3 - 1]
                else:
                    v2[v4] = 0
                    v4 += 1
            return v2

        def count_matches(a1, a2):
            v1 = len(a2)
            if v1 == 0:
                return len(a1) + 1
            v2 = longest_prefix_suffix(a2)
            v3 = 0
            v4 = 0
            v5 = 0
            while v4 < len(a1):
                if v5 < v1 and a2[v5] == a1[v4]:
                    v4 += 1
                    v5 += 1
                if v5 == v1:
                    v3 += 1
                    v5 = v2[v5 - 1]
                elif v4 < len(a1) and (v5 == 0 or a2[v5] != a1[v4]):
                    if v5 > 0:
                        v5 = v2[v5 - 1]
                    else:
                        v4 += 1
            return v3
        return count_matches(v2, a2)
