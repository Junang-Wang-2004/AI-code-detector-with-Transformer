class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, a1):

        def generate_trees(a1):
            if a1 % 2 == 0 or a1 < 1:
                return []
            if a1 == 1:
                return [C1()]
            if a1 in self.cache:
                return self.cache[a1]
            v1 = []
            for v2 in range(1, a1, 2):
                v3 = generate_trees(v2)
                v4 = generate_trees(a1 - 1 - v2)
                for v5 in v3:
                    for v6 in v4:
                        v7 = C1()
                        v7.left = v5
                        v7.right = v6
                        v1.append(v7)
            self.cache[a1] = v1
            return v1
        return generate_trees(a1)
