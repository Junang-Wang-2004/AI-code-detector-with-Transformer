class C1:

    def checkArithmeticSubarrays(self, a1, a2, a3):

        def check_ap(a1):
            v1 = sorted(a1)
            v2 = len(v1)
            if v2 <= 1:
                return True
            v3 = v1[1] - v1[0]
            return all((v1[k] - v1[k - 1] == v3 for v4 in range(1, v2)))
        return [check_ap(a1[start:end + 1]) for v1, v2 in zip(a2, a3)]
