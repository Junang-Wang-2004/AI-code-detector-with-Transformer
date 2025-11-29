class C1:

    def isMajorityElement(self, a1, a2):

        def lower(a1, a2):
            v1, v2 = (0, len(a1))
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] < a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1

        def upper(a1, a2):
            v1, v2 = (0, len(a1))
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] <= a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1
        v1 = upper(a1, a2) - lower(a1, a2)
        return v1 * 2 > len(a1)
