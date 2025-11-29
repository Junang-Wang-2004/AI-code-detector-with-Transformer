class C1:

    def kIncreasing(self, a1, a2):

        def nondec_lis_length(a1):
            v1 = []
            for v2 in a1:
                v3 = 0
                while v3 < len(v1) and v1[v3] <= v2:
                    v3 += 1
                if v3 == len(v1):
                    v1.append(v2)
                else:
                    v1[v3] = v2
            return len(v1)
        v1 = len(a1)
        v2 = 0
        for v3 in range(a2):
            v4 = a1[v3::a2]
            v2 += nondec_lis_length(v4)
        return v1 - v2
