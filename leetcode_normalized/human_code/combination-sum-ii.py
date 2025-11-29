class C1(object):

    def combinationSum2(self, a1, a2):
        v1 = []
        self.combinationSumRecu(sorted(a1), v1, 0, [], a2)
        return v1

    def combinationSumRecu(self, a1, a2, a3, a4, a5):
        if a5 == 0:
            a2.append(list(a4))
        v1 = 0
        while a3 < len(a1) and a1[a3] <= a5:
            if v1 != a1[a3]:
                a4.append(a1[a3])
                self.combinationSumRecu(a1, a2, a3 + 1, a4, a5 - a1[a3])
                a4.pop()
                v1 = a1[a3]
            a3 += 1
