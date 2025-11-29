class C1(object):

    def permuteUnique(self, a1):
        """
        """
        a1.sort()
        v1 = []
        v2 = [False] * len(a1)
        self.permuteUniqueRecu(v1, v2, [], a1)
        return v1

    def permuteUniqueRecu(self, a1, a2, a3, a4):
        if len(a3) == len(a4):
            a1.append(a3 + [])
            return
        for v1 in range(len(a4)):
            if a2[v1] or (v1 > 0 and a4[v1 - 1] == a4[v1] and (not a2[v1 - 1])):
                continue
            a2[v1] = True
            a3.append(a4[v1])
            self.permuteUniqueRecu(a1, a2, a3, a4)
            a3.pop()
            a2[v1] = False
