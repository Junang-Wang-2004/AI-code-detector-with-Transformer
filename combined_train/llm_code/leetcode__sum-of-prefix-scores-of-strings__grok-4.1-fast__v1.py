class C1:

    def __init__(self):
        self.children = {}
        self.pass_count = 0

class C2:

    def sumPrefixScores(self, a1):
        v1 = C1()
        for v2 in a1:
            v3 = v1
            for v4 in v2:
                if v4 not in v3.children:
                    v3.children[v4] = C1()
                v3 = v3.children[v4]
                v3.pass_count += 1
        v5 = []
        for v2 in a1:
            v6 = 0
            v3 = v1
            for v4 in v2:
                v3 = v3.children[v4]
                v6 += v3.pass_count
            v5.append(v6)
        return v5
