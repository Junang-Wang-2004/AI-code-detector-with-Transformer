class C1(object):

    def countSubarrays(self, a1, a2):
        v1 = a1.index(a2)

        def get_score(a1):
            if a1 == a2:
                return 0
            elif a1 < a2:
                return -1
            else:
                return 1
        v2 = {0: 1}
        v3 = 0
        for v4 in range(v1):
            v3 += get_score(a1[v4])
            v2[v3] = v2.get(v3, 0) + 1
        v3 += get_score(a1[v1])
        v5 = v2.get(v3, 0) + v2.get(v3 - 1, 0)
        for v4 in range(v1 + 1, len(a1)):
            v3 += get_score(a1[v4])
            v5 += v2.get(v3, 0) + v2.get(v3 - 1, 0)
        return v5
