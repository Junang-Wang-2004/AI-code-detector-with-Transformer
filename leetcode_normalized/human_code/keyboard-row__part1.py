class C1(object):

    def findWords(self, a1):
        """
        """
        v1 = [set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']), set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']), set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])]
        v2 = []
        for v3 in a1:
            v4 = 0
            for v5 in range(len(v1)):
                if v3[0].lower() in v1[v5]:
                    v4 = v5
                    break
            for v6 in v3:
                if v6.lower() not in v1[v4]:
                    break
            else:
                v2.append(v3)
        return v2
