class C1(object):

    def areSentencesSimilar(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            a1, a2 = (a2, a1)
        v3 = 0
        for v4 in (lambda x: x, lambda x: -1 - x):
            for v5 in range(len(a1) + 1):
                v6 = a1[v4(v5)] if v5 != len(a1) else ' '
                v7 = a2[v4(v5)] if v5 != len(a2) else ' '
                if v6 != v7:
                    break
                if v6 == ' ':
                    v3 += 1
        return v3 >= a1.count(' ') + 1
