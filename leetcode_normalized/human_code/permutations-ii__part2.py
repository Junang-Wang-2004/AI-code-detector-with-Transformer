class C1(object):

    def permuteUnique(self, a1):
        v1 = [[]]
        for v2 in a1:
            next = []
            for v3 in v1:
                for v4 in range(len(v3) + 1):
                    v5 = v3[:v4] + [v2] + v3[v4:]
                    if v5 not in next:
                        next.append(v5)
            v1 = next
        return v1
