class C1:

    def areSentencesSimilar(self, a1, a2):
        v1 = a1.split()
        v2 = a2.split()
        v3, v4 = (len(v1), len(v2))
        v5 = 0
        while v5 < min(v3, v4) and v1[v5] == v2[v5]:
            v5 += 1
        v6 = 0
        while v6 < min(v3, v4) and v1[v3 - 1 - v6] == v2[v4 - 1 - v6]:
            v6 += 1
        return v5 + v6 >= min(v3, v4)
