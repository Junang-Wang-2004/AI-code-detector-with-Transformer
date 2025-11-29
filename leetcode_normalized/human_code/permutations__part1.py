class C1(object):

    def permute(self, a1):
        v1 = []
        v2 = [False] * len(a1)
        self.permuteRecu(v1, v2, [], a1)
        return v1

    def permuteRecu(self, a1, a2, a3, a4):
        if len(a3) == len(a4):
            a1.append(a3[:])
            return
        for v1 in range(len(a4)):
            if not a2[v1]:
                a2[v1] = True
                a3.append(a4[v1])
                self.permuteRecu(a1, a2, a3, a4)
                a3.pop()
                a2[v1] = False
