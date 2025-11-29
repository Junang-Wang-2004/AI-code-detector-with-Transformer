class C1(object):

    def secondGreaterElement(self, a1):
        v1 = [-1] * len(a1)
        v2 = []
        v3 = []
        for v4 in range(len(a1)):
            v5 = a1[v4]
            while v3 and a1[v3[-1]] < v5:
                v1[v3.pop()] = v5
            v6 = []
            while v2 and a1[v2[-1]] < v5:
                v6.append(v2.pop())
            v2.append(v4)
            while v6:
                v3.append(v6.pop())
        return v1
