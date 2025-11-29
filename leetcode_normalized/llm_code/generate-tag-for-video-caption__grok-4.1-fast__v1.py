class C1:

    def generateTag(self, a1):
        v1 = 100
        v2 = []
        v3 = a1.split()
        if v3:
            v2.append(v3[0].lower())
            for v4 in v3[1:]:
                if v4:
                    v2.append(v4[0].upper() + v4[1:].lower())
        v5 = '#' + ''.join(v2)
        return v5[:v1]
