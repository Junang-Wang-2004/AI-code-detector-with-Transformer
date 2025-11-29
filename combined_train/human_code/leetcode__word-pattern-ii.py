class C1(object):

    def wordPatternMatch(self, a1, a2):
        """
        """
        v1, v2 = ({}, {})
        return self.match(a1, a2, 0, 0, v1, v2)

    def match(self, a1, a2, a3, a4, a5, a6):
        v1 = False
        if a3 == len(a1) and a4 == len(a2):
            v1 = True
        elif a3 < len(a1) and a4 < len(a2):
            v2 = a1[a3]
            if v2 in a6:
                v3 = a6[v2]
                if v3 == a2[a4:a4 + len(v3)]:
                    v1 = self.match(a1, a2, a3 + 1, a4 + len(v3), a5, a6)
            else:
                for v4 in range(a4, len(a2)):
                    v3 = a2[a4:v4 + 1]
                    if v3 not in a5:
                        a5[v3], a6[v2] = (v2, v3)
                        v1 = self.match(a1, a2, a3 + 1, v4 + 1, a5, a6)
                        (a5.pop(v3), a6.pop(v2))
                    if v1:
                        break
        return v1
