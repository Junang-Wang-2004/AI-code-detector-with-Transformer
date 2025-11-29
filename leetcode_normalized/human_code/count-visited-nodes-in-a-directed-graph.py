class C1(object):

    def countVisitedNodes(self, a1):
        """
        """

        def find_cycles(a1):
            v1 = [0] * len(a1)
            v2 = [0] * len(a1)
            v3 = []
            v4 = 0
            for v5 in range(len(a1)):
                v6 = v4
                while not v2[v5]:
                    v4 += 1
                    v2[v5] = v4
                    v3.append(v5)
                    v5 = a1[v5]
                if v2[v5] > v6:
                    v7 = v4 - v2[v5] + 1
                    for v8 in range(v7):
                        v1[v3.pop()] = v7
                while v3:
                    v1[v3[-1]] = v1[a1[v3[-1]]] + 1
                    v3.pop()
            return v1
        return find_cycles(a1)
