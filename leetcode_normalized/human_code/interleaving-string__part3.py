class C1(object):

    def isInterleave(self, a1, a2, a3):
        self.match = {}
        if len(a1) + len(a2) != len(a3):
            return False
        return self.isInterleaveRecu(a1, a2, a3, 0, 0, 0)

    def isInterleaveRecu(self, a1, a2, a3, a4, a5, a6):
        if repr([a4, a5]) in list(self.match.keys()):
            return self.match[repr([a4, a5])]
        if a6 == len(a3):
            return True
        v1 = False
        if a4 < len(a1) and a1[a4] == a3[a6]:
            v1 = v1 or self.isInterleaveRecu(a1, a2, a3, a4 + 1, a5, a6 + 1)
        if a5 < len(a2) and a2[a5] == a3[a6]:
            v1 = v1 or self.isInterleaveRecu(a1, a2, a3, a4, a5 + 1, a6 + 1)
        self.match[repr([a4, a5])] = v1
        return v1
