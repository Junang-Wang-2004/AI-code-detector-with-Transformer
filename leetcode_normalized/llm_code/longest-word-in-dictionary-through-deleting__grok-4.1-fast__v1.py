class C1:

    def findLongestWord(self, a1, a2):
        v1 = ''
        for v2 in a2:
            v3 = 0
            v4 = True
            for v5 in v2:
                v3 = a1.find(v5, v3)
                if v3 == -1:
                    v4 = False
                    break
                v3 += 1
            if v4 and (len(v2) > len(v1) or (len(v2) == len(v1) and v2 < v1)):
                v1 = v2
        return v1
