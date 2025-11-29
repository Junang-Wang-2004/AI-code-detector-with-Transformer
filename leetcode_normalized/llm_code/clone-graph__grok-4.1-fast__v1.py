class C1(object):

    def __init__(self, a1):
        self.label = a1
        self.neighbors = []

class C2(object):

    def cloneGraph(self, a1):
        if not a1:
            return None
        v1 = {}

        def build_copy(a1):
            if a1 in v1:
                return v1[a1]
            v1 = C1(a1.label)
            v1[a1] = v1
            for v2 in a1.neighbors:
                v1.neighbors.append(build_copy(v2))
            return v1
        return build_copy(a1)
