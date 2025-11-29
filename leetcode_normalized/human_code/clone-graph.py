class C1(object):

    def __init__(self, a1):
        self.label = a1
        self.neighbors = []

class C2(object):

    def cloneGraph(self, a1):
        if a1 is None:
            return None
        v1 = C1(a1.label)
        v2, v3 = ({a1: v1}, [a1])
        while v3:
            v4 = v3.pop()
            for v5 in v4.neighbors:
                if v5 not in v2:
                    v3.append(v5)
                    v6 = C1(v5.label)
                    v2[v5] = v6
                v2[v4].neighbors.append(v2[v5])
        return v2[a1]
