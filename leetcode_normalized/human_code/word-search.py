class C1(object):

    def exist(self, a1, a2):
        v1 = [[False for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
        for v3 in range(len(a1)):
            for v2 in range(len(a1[0])):
                if self.existRecu(a1, a2, 0, v3, v2, v1):
                    return True
        return False

    def existRecu(self, a1, a2, a3, a4, a5, a6):
        if a3 == len(a2):
            return True
        if a4 < 0 or a4 >= len(a1) or a5 < 0 or (a5 >= len(a1[0])) or a6[a4][a5] or (a1[a4][a5] != a2[a3]):
            return False
        a6[a4][a5] = True
        v1 = self.existRecu(a1, a2, a3 + 1, a4 + 1, a5, a6) or self.existRecu(a1, a2, a3 + 1, a4 - 1, a5, a6) or self.existRecu(a1, a2, a3 + 1, a4, a5 + 1, a6) or self.existRecu(a1, a2, a3 + 1, a4, a5 - 1, a6)
        a6[a4][a5] = False
        return v1
