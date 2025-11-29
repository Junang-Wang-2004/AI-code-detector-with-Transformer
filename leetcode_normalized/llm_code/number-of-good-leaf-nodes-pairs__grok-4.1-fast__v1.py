class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def countPairs(self, a1, a2):
        self.res = 0

        def process(a1):
            if a1 is None:
                return {}
            if a1.left is None and a1.right is None:
                return {0: 1}
            v1 = process(a1.left)
            v2 = process(a1.right)
            for v3 in v1:
                for v4 in v2:
                    if v3 + v4 + 2 <= a2:
                        self.res += v1[v3] * v2[v4]
            v5 = {}
            for v6, v7 in v1.items():
                v5[v6 + 1] = v5.get(v6 + 1, 0) + v7
            for v6, v7 in v2.items():
                v5[v6 + 1] = v5.get(v6 + 1, 0) + v7
            return v5
        process(a1)
        return self.res
