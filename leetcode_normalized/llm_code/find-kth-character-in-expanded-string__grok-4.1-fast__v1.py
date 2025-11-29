class C1:

    def kthCharacter(self, a1, a2):
        v1 = 0
        v2 = 0
        for v3 in a1:
            if v3 == ' ':
                v4 = 1
                v1 = 0
            else:
                v1 += 1
                v4 = v1
            v2 += v4
            if v2 >= a2:
                return v3
