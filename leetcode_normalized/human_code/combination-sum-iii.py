class C1(object):

    def combinationSum3(self, a1, a2):
        v1 = []
        self.combinationSumRecu(v1, [], 1, a1, a2)
        return v1

    def combinationSumRecu(self, a1, a2, a3, a4, a5):
        if a4 == 0 and a5 == 0:
            a1.append(list(a2))
        elif a4 < 0:
            return
        while a3 < 10 and a3 * a4 + a4 * (a4 - 1) / 2 <= a5:
            a2.append(a3)
            self.combinationSumRecu(a1, a2, a3 + 1, a4 - 1, a5 - a3)
            a2.pop()
            a3 += 1
